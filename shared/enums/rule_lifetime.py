"""Rule lifetime enumeration."""

from enum import Enum


class RuleLifetime(str, Enum):
    """Firewall rule lifetime."""
    
    PERMANENT = "permanent"
    TEMPORARY = "temporary"