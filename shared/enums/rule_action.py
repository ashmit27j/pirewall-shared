"""Rule action enumeration."""

from enum import Enum


class RuleAction(str, Enum):
    """Firewall rule actions."""
    
    BLOCK = "block"
    ALLOW = "allow"
    RATE_LIMIT = "rate_limit"
    REJECT = "reject"