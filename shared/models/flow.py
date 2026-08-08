"""Flow model for network traffic observation."""

from __future__ import annotations

from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, validator, model_validator
from ipaddress import ip_address
import uuid

from shared.enums import ProtocolType, ConnectionState


class Flow(BaseModel):
    """The canonical network observation object used throughout the Pirewall ecosystem."""

    # Identification
    flow_id: str = Field(..., description="Globally unique identifier for the flow")
    flow_version: str = Field("1.0", description="Schema version of the flow")

    # Network
    source_ip: str = Field(..., description="Source IP address")
    destination_ip: str = Field(..., description="Destination IP address")
    source_port: int = Field(..., description="Source port number")
    destination_port: int = Field(..., description="Destination port number")
    protocol: ProtocolType = Field(..., description="Network protocol")

    # Timing
    start_timestamp: datetime = Field(..., description="Flow start time")
    end_timestamp: datetime = Field(..., description="Flow end time")
    duration: float = Field(..., description="Duration in seconds")

    # Volume
    total_packets: int = Field(..., description="Total number of packets")
    total_bytes: int = Field(..., description="Total number of bytes")
    forward_packets: int = Field(..., description="Forward packets count")
    reverse_packets: int = Field(..., description="Reverse packets count")
    forward_bytes: int = Field(..., description="Forward bytes count")
    reverse_bytes: int = Field(..., description="Reverse bytes count")

    # Transport
    tcp_flags_summary: Optional[str] = Field(None, description="TCP flags summary")
    connection_state: ConnectionState = Field(..., description="Connection state")

    # Feature vector - stored as list of numerical features
    feature_vector: List[float] = Field(..., description="Extracted numerical features")

    # Metadata
    interface_name: Optional[str] = Field(None, description="Interface name")
    vlan_id: Optional[int] = Field(None, description="VLAN ID")
    capture_source: Optional[str] = Field(None, description="Capture source identifier")
    sensor_identifier: Optional[str] = Field(None, description="Sensor identifier")

    class Config:
        """Pydantic configuration."""
        use_enum_values = True
        validate_assignment = True

    @validator('source_ip', 'destination_ip')
    def validate_ip_address(cls, v):
        """Validate IP address format."""
        try:
            ip_address(v)
            return v
        except ValueError:
            raise ValueError(f"Invalid IP address: {v}")

    @validator('source_port', 'destination_port')
    def validate_port(cls, v):
        """Validate port number."""
        if not 0 <= v <= 65535:
            raise ValueError("Port must be between 0 and 65535")
        return v

    @validator('protocol')
    def validate_protocol(cls, v):
        """Validate protocol type."""
        # Protocol validation is handled by the enum
        return v

    @validator('total_packets')
    def validate_total_packets(cls, v):
        """Validate total packets count."""
        if v < 1:
            raise ValueError("Total packets must be at least 1")
        return v

    @validator('total_bytes', 'forward_bytes', 'reverse_bytes')
    def validate_byte_counts(cls, v):
        """Validate byte counts."""
        if v < 0:
            raise ValueError("Byte count cannot be negative")
        return v

    @validator('end_timestamp')
    def validate_timestamps(cls, v, values):
        """Validate that end timestamp is after start timestamp."""
        if 'start_timestamp' in values and v < values['start_timestamp']:
            raise ValueError("End timestamp must be after start timestamp")
        return v

    @model_validator(mode='after')
    def validate_flow_fields(self):
        """Validate flow fields."""
        # Validate that forward and reverse packets sum to total packets
        if (self.forward_packets + self.reverse_packets != 
            self.total_packets):
            raise ValueError("Forward and reverse packets must sum to total packets")
        
        # Validate that forward and reverse bytes sum to total bytes
        if (self.forward_bytes + self.reverse_bytes != 
            self.total_bytes):
            raise ValueError("Forward and reverse bytes must sum to total bytes")
        
        return self

    def __init__(self, **data):
        """Initialize Flow with automatic ID generation if not provided."""
        if 'flow_id' not in data:
            # Generate a UUID for the flow ID
            data['flow_id'] = str(uuid.uuid4())
        super().__init__(**data)