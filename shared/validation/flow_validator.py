"""Flow validation utilities."""

from typing import Any
from shared.models.flow import Flow


def validate_flow(flow: Flow) -> bool:
    """Validate a Flow object.
    
    Args:
        flow: The Flow object to validate
        
    Returns:
        True if valid, False otherwise
    """
    try:
        # This will trigger Pydantic validation internally
        _ = Flow(**flow.dict())
        return True
    except Exception:
        return False


def validate_flow_dict(flow_dict: dict[str, Any]) -> bool:
    """Validate a Flow dictionary.
    
    Args:
        flow_dict: Dictionary representation of a Flow
        
    Returns:
        True if valid, False otherwise
    """
    try:
        _ = Flow(**flow_dict)
        return True
    except Exception:
        return False