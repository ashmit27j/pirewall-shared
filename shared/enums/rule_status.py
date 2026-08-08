"""Rule status enumeration."""

from enum import Enum


class RuleStatus(str, Enum):
    """Firewall rule status."""
    
    PENDING = "pending"
    ACTIVE = "active"
    EXPIRED = "expired"
    DISABLED = "disabled"