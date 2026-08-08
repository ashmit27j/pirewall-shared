"""Rule scope enumeration."""

from enum import Enum


class RuleScope(str, Enum):
    """Firewall rule scope."""
    
    INTERFACE = "interface"
    DIRECTION = "direction"
    PROTOCOL = "protocol"