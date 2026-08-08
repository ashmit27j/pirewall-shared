"""Host State model for tracking host information."""

from __future__ import annotations

from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field


class HostState(BaseModel):
    """State information about a network host."""

    # Metadata
    host_id: str = Field(..., description="Unique identifier for the host")
    timestamp: datetime = Field(..., description="Timestamp of the state record")
    
    # Host identification
    ip_address: str = Field(..., description="IP address of the host")
    mac_address: Optional[str] = Field(None, description="MAC address of the host")
    
    # Host characteristics
    hostname: Optional[str] = Field(None, description="Hostname if known")
    operating_system: Optional[str] = Field(None, description="Operating system if detected")
    device_type: Optional[str] = Field(None, description="Type of device (PC, mobile, IoT, etc.)")
    
    # Network behavior
    connection_count: int = Field(..., description="Number of active connections")
    total_bytes_sent: int = Field(..., description="Total bytes sent by the host")
    total_bytes_received: int = Field(..., description="Total bytes received by the host")
    
    # Security state
    last_seen: datetime = Field(..., description="Timestamp when host was last seen")
    is_trusted: bool = Field(..., description="Whether the host is trusted")
    
    # Additional metadata
    attributes: Dict[str, Any] = Field(default_factory=dict, description="Additional host attributes")

    class Config:
        """Pydantic configuration."""
        use_enum_values = True
        validate_assignment = True