"""Risk level enumeration."""

from enum import Enum


class RiskLevel(str, Enum):
    """Risk level classifications."""
    
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"