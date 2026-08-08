#!/usr/bin/env python3
"""Simple test of our shared models."""

from datetime import datetime
import sys

try:
    from shared.models.flow import Flow
    from shared.models.threat_assessment import ThreatAssessment
    from shared.models.firewall_rule import FirewallRule
    from shared.enums import ProtocolType, ConnectionState, RiskLevel, SecurityRecommendation
    from shared.enums import RuleAction, RuleStatus
    
    print("All imports successful")
    
    # Test Flow model
    flow = Flow(
        source_ip="192.168.1.1",
        destination_ip="10.0.0.1", 
        source_port=12345,
        destination_port=80,
        protocol=ProtocolType.TCP,
        start_timestamp=datetime.now(),
        end_timestamp=datetime.now(),
        duration=1.0,
        total_packets=10,
        total_bytes=1000,
        forward_packets=5,
        reverse_packets=5,
        forward_bytes=500,
        reverse_bytes=500,
        connection_state=ConnectionState.ESTABLISHED,
        feature_vector=[1.0, 2.0, 3.0],
    )
    
    print("Flow model creation successful")
    print(f"Flow ID: {flow.flow_id}")
    print(f"Protocol: {flow.protocol}")
    
    # Test ThreatAssessment model
    assessment = ThreatAssessment(
        assessment_id="test-assessment-123",
        parent_flow_id="test-flow-456",
        timestamp=datetime.now(),
        overall_risk_level=RiskLevel.HIGH,
        overall_confidence=0.95,
        reasons=["Known attack pattern detected", "High anomaly score"],
        recommendation=SecurityRecommendation.TEMPORARY_BLOCK,
    )
    
    print("ThreatAssessment model creation successful")
    print(f"Risk Level: {assessment.overall_risk_level}")
    print(f"Confidence: {assessment.overall_confidence}")
    
    # Test FirewallRule model
    rule = FirewallRule(
        rule_id="test-rule-789",
        creation_timestamp=datetime.now(),
        source="system",
        match_type="ip",
        match_value="10.0.0.1",
        action=RuleAction.BLOCK,
        permanent=True,
        status=RuleStatus.ACTIVE,
    )
    
    print("FirewallRule model creation successful")
    print(f"Rule Action: {rule.action}")
    print(f"Rule Status: {rule.status}")
    
    print("\nAll basic tests passed!")
    sys.exit(0)
    
except Exception as e:
    print(f"Test failed with error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)