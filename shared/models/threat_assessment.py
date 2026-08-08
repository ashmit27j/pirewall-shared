"""Threat Assessment model for security evaluation."""

from __future__ import annotations

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, validator
from enum import Enum

from shared.enums import RiskLevel, ConfidenceLevel, SecurityRecommendation


class ThreatAssessment(BaseModel):
    """Unified security evaluation produced by combining all available evidence sources."""

    # Metadata
    assessment_id: str = Field(..., description="Unique identifier for the assessment")
    parent_flow_id: str = Field(..., description="ID of the flow being assessed")
    timestamp: datetime = Field(..., description="Timestamp of the assessment")

    # Risk
    overall_risk_level: RiskLevel = Field(..., description="Overall risk level")
    overall_confidence: float = Field(..., description="Confidence in the assessment (0.0-1.0)")

    # Evidence Summary
    known_evidence_reference: Optional[str] = Field(None, description="Reference to known evidence")
    anomaly_evidence_reference: Optional[str] = Field(None, description="Reference to anomaly evidence")
    behavior_evidence_reference: Optional[str] = Field(None, description="Reference to behavior evidence")

    # Reasoning
    reasons: List[str] = Field(..., description="Human-readable reasons supporting the assessment")

    # Recommendations
    recommendation: SecurityRecommendation = Field(..., description="Suggested security posture")

    class Config:
        """Pydantic configuration."""
        use_enum_values = True
        validate_assignment = True

    @validator('overall_confidence')
    def validate_confidence(cls, v):
        """Validate confidence is between 0.0 and 1.0."""
        if not 0.0 <= v <= 1.0:
            raise ValueError("Confidence must be between 0.0 and 1.0")
        return v

    @validator('reasons')
    def validate_reasons(cls, v):
        """Validate reasons list is not empty."""
        if not v:
            raise ValueError("Reasons list cannot be empty")
        return v