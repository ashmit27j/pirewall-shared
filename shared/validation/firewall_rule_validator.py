"""Firewall Rule validation utilities."""

from typing import Any
from shared.models.firewall_rule import FirewallRule


def validate_firewall_rule(firewall_rule: FirewallRule) -> bool:
    """Validate a FirewallRule object.
    
    Args:
        firewall_rule: The FirewallRule object to validate
        
    Returns:
        True if valid, False otherwise
    """
    try:
        # This will trigger Pydantic validation internally
        _ = FirewallRule(**firewall_rule.dict())
        return True
    except Exception:
        return False


def validate_firewall_rule_dict(firewall_rule_dict: dict[str, Any]) -> bool:
    """Validate a FirewallRule dictionary.
    
    Args:
        firewall_rule_dict: Dictionary representation of a FirewallRule
        
    Returns:
        True if valid, False otherwise
    """
    try:
        _ = FirewallRule(**firewall_rule_dict)
        return True
    except Exception:
        return False