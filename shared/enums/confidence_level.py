"""Confidence level enumeration."""

from enum import Enum


class ConfidenceLevel(str, Enum):
    """Confidence level classifications."""
    
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    VERY_HIGH = "very_high"