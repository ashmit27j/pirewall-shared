#!/usr/bin/env python3
"""Comprehensive test of all shared components."""

from datetime import datetime
import sys

try:
    # Test imports
    from shared.models import *
    from shared.enums import *
    from shared.validation import *
    from shared.serialization import *
    from shared.exceptions import *
    from shared.constants import *
    
    print("✓ All imports successful")
    
    # Test all models
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
    
    print("✓ Flow model creation successful")
    
    assessment = ThreatAssessment(
        assessment_id="test-assessment-123",
        parent_flow_id="test-flow-456",
        timestamp=datetime.now(),
        overall_risk_level=RiskLevel.HIGH,
        overall_confidence=0.95,
        reasons=["Known attack pattern detected", "High anomaly score"],
        recommendation=SecurityRecommendation.TEMPORARY_BLOCK,
    )
    
    print("✓ ThreatAssessment model creation successful")
    
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
    
    print("✓ FirewallRule model creation successful")
    
    # Test serialization
    json_str = serialize_model(flow)
    deserialized_flow = deserialize_model(Flow, json_str)
    print("✓ Serialization/Deserialization round-trip successful")
    
    # Test validation
    is_valid = validate_flow(flow)
    print(f"✓ Flow validation successful: {is_valid}")
    
    # Test enums
    assert ProtocolType.TCP == "tcp"
    assert RiskLevel.HIGH == "high"
    assert RuleAction.BLOCK == "block"
    print("✓ Enum values correct")
    
    # Test constants
    assert SHARED_VERSION == "0.1.0"
    assert HIGH_RISK_THRESHOLD == 0.8
    print("✓ Constants correct")
    
    print("\n🎉 All comprehensive tests passed!")
    sys.exit(0)
    
except Exception as e:
    print(f"✗ Comprehensive test failed with error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)