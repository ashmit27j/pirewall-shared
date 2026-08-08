"""Threat Assessment validation utilities."""

from typing import Any
from shared.models.threat_assessment import ThreatAssessment


def validate_threat_assessment(threat_assessment: ThreatAssessment) -> bool:
    """Validate a ThreatAssessment object.
    
    Args:
        threat_assessment: The ThreatAssessment object to validate
        
    Returns:
        True if valid, False otherwise
    """
    try:
        # This will trigger Pydantic validation internally
        _ = ThreatAssessment(**threat_assessment.dict())
        return True
    except Exception:
        return False


def validate_threat_assessment_dict(threat_assessment_dict: dict[str, Any]) -> bool:
    """Validate a ThreatAssessment dictionary.
    
    Args:
        threat_assessment_dict: Dictionary representation of a ThreatAssessment
        
    Returns:
        True if valid, False otherwise
    """
    try:
        _ = ThreatAssessment(**threat_assessment_dict)
        return True
    except Exception:
        return False