"""Firewall Rule model for network filtering rules."""

from __future__ import annotations

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, validator
from enum import Enum

from shared.enums import RuleAction, RuleScope, RuleLifetime, RuleStatus


class FirewallRule(BaseModel):
    """Executable network filtering rule enforced by the Raspberry Pi."""

    # Metadata
    rule_id: str = Field(..., description="Unique identifier for the rule")
    creation_timestamp: datetime = Field(..., description="Timestamp of rule creation")
    source: str = Field(..., description="Source of the rule (administrator, system, etc.)")

    # Target
    match_type: str = Field(..., description="Type of match (ip, port, protocol, etc.)")
    match_value: str = Field(..., description="Value to match against")

    # Action
    action: RuleAction = Field(..., description="Action to take (block, allow, etc.)")

    # Scope
    interface: Optional[str] = Field(None, description="Interface to apply rule to")
    direction: Optional[str] = Field(None, description="Direction of traffic (in, out)")
    protocol: Optional[str] = Field(None, description="Protocol to match")

    # Lifetime
    permanent: bool = Field(..., description="Whether the rule is permanent")
    expiration_time: Optional[datetime] = Field(None, description="Expiration timestamp if not permanent")

    # Status
    status: RuleStatus = Field(..., description="Current status of the rule")

    class Config:
        """Pydantic configuration."""
        use_enum_values = True
        validate_assignment = True

    @validator('expiration_time')
    def validate_expiration(cls, v, values):
        """Validate expiration time if not permanent."""
        if not values.get('permanent', True) and v is None:
            raise ValueError("Expiration time required for non-permanent rules")
        return v