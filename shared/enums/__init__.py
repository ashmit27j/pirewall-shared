"""Shared enumerations for the pirewall project."""

from .protocol import ProtocolType
from .connection_state import ConnectionState
from .risk_level import RiskLevel
from .confidence_level import ConfidenceLevel
from .security_recommendation import SecurityRecommendation
from .rule_action import RuleAction
from .rule_scope import RuleScope
from .rule_lifetime import RuleLifetime
from .rule_status import RuleStatus

__all__ = [
    'ProtocolType',
    'ConnectionState',
    'RiskLevel',
    'ConfidenceLevel',
    'SecurityRecommendation',
    'RuleAction',
    'RuleScope',
    'RuleLifetime',
    'RuleStatus',
]