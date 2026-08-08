"""System Status model for tracking system health."""

from __future__ import annotations

from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field


class SystemStatus(BaseModel):
    """System status information for monitoring and diagnostics."""

    # Metadata
    status_id: str = Field(..., description="Unique identifier for the status record")
    timestamp: datetime = Field(..., description="Timestamp of the status report")
    
    # System health indicators
    cpu_usage: float = Field(..., description="CPU usage percentage (0.0-100.0)")
    memory_usage: float = Field(..., description="Memory usage percentage (0.0-100.0)")
    disk_usage: float = Field(..., description="Disk usage percentage (0.0-100.0)")
    
    # Component status
    packet_capture_active: bool = Field(..., description="Whether packet capture is active")
    flow_generation_active: bool = Field(..., description="Whether flow generation is active")
    inference_engine_active: bool = Field(..., description="Whether inference engine is active")
    threat_scoring_active: bool = Field(..., description="Whether threat scoring is active")
    
    # System metrics
    uptime_seconds: int = Field(..., description="System uptime in seconds")
    total_flows_processed: int = Field(..., description="Total flows processed since start")
    total_threats_detected: int = Field(..., description="Total threats detected since start")
    
    # Additional metadata
    additional_info: Dict[str, Any] = Field(default_factory=dict, description="Additional status information")

    class Config:
        """Pydantic configuration."""
        use_enum_values = True
        validate_assignment = True