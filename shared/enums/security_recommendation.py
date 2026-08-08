"""Security recommendation enumeration."""

from enum import Enum


class SecurityRecommendation(str, Enum):
    """Suggested security posture recommendations."""
    
    ALLOW = "allow"
    MONITOR = "monitor"
    RATE_LIMIT = "rate_limit"
    TEMPORARY_BLOCK = "temporary_block"
    PERMANENT_BLOCK = "permanent_block"