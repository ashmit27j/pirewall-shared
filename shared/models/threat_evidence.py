"""Threat Evidence model for known threat information."""

from __future__ import annotations

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class ThreatEvidence(BaseModel):
    """Evidence of known threats detected in a flow."""

    # Metadata
    evidence_id: str = Field(..., description="Unique identifier for the evidence")
    parent_flow_id: str = Field(..., description="ID of the flow this evidence relates to")
    timestamp: datetime = Field(..., description="Timestamp when evidence was generated")

    # Threat information
    threat_type: str = Field(..., description="Type of threat detected")
    threat_category: str = Field(..., description="Category of the threat")
    threat_source: Optional[str] = Field(None, description="Source of the threat information")
    threat_signature: Optional[str] = Field(None, description="Signature or pattern of the threat")

    # Detection details
    detection_confidence: float = Field(..., description="Confidence in the detection (0.0-1.0)")
    detection_source: str = Field(..., description="Source of the detection")
    
    # Additional metadata
    references: List[str] = Field(default_factory=list, description="References to threat databases or reports")

    class Config:
        """Pydantic configuration."""
        use_enum_values = True
        validate_assignment = True