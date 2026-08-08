"""Tests for shared models."""

import pytest
from datetime import datetime
from uuid import UUID

from shared.models.flow import Flow
from shared.models.threat_assessment import ThreatAssessment
from shared.models.firewall_rule import FirewallRule
from shared.models.threat_evidence import ThreatEvidence
from shared.models.behavior_evidence import BehaviorEvidence
from shared.models.policy_recommendation import PolicyRecommendation
from shared.models.host_state import HostState
from shared.models.system_status import SystemStatus
from shared.models.model_metadata import ModelMetadata

from shared.enums import ProtocolType, ConnectionState, RiskLevel, SecurityRecommendation
from shared.enums import RuleAction, RuleScope, RuleLifetime, RuleStatus


def test_flow_model():
    """Test Flow model creation and validation."""
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
    
    # Test that flow_id was auto-generated
    assert isinstance(flow.flow_id, str)
    assert UUID(flow.flow_id)  # Should be a valid UUID
    
    # Test that all required fields are present
    assert flow.source_ip == "192.168.1.1"
    assert flow.destination_ip == "10.0.0.1"
    assert flow.protocol == ProtocolType.TCP


def test_threat_assessment_model():
    """Test ThreatAssessment model creation and validation."""
    assessment = ThreatAssessment(
        assessment_id="test-assessment-123",
        parent_flow_id="test-flow-456",
        timestamp=datetime.now(),
        overall_risk_level=RiskLevel.HIGH,
        overall_confidence=0.95,
        reasons=["Known attack pattern detected", "High anomaly score"],
        recommendation=SecurityRecommendation.TEMPORARY_BLOCK,
    )
    
    assert assessment.assessment_id == "test-assessment-123"
    assert assessment.overall_risk_level == RiskLevel.HIGH
    assert assessment.overall_confidence == 0.95
    assert len(assessment.reasons) == 2


def test_firewall_rule_model():
    """Test FirewallRule model creation and validation."""
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
    
    assert rule.rule_id == "test-rule-789"
    assert rule.action == RuleAction.BLOCK
    assert rule.permanent is True


def test_threat_evidence_model():
    """Test ThreatEvidence model creation."""
    evidence = ThreatEvidence(
        evidence_id="test-evidence-123",
        parent_flow_id="test-flow-456",
        timestamp=datetime.now(),
        threat_type="malware",
        threat_category="trojan",
        detection_confidence=0.9,
        detection_source="signature-db",
    )
    
    assert evidence.evidence_id == "test-evidence-123"
    assert evidence.threat_type == "malware"


def test_behavior_evidence_model():
    """Test BehaviorEvidence model creation."""
    evidence = BehaviorEvidence(
        evidence_id="test-behavior-123",
        parent_flow_id="test-flow-456",
        timestamp=datetime.now(),
        behavior_type="scan",
        behavior_category="port_scan",
        anomaly_score=0.85,
        detection_confidence=0.8,
        detection_source="anomaly-detection-engine",
    )
    
    assert evidence.evidence_id == "test-behavior-123"
    assert evidence.behavior_type == "scan"


def test_policy_recommendation_model():
    """Test PolicyRecommendation model creation."""
    recommendation = PolicyRecommendation(
        recommendation_id="test-rec-123",
        timestamp=datetime.now(),
        source="policy-engine",
        recommended_action="block",
        reason="Suspicious behavior detected",
        confidence=0.75,
    )
    
    assert recommendation.recommendation_id == "test-rec-123"
    assert recommendation.confidence == 0.75


def test_host_state_model():
    """Test HostState model creation."""
    host = HostState(
        host_id="test-host-123",
        timestamp=datetime.now(),
        ip_address="192.168.1.100",
        connection_count=5,
        total_bytes_sent=10000,
        total_bytes_received=20000,
        last_seen=datetime.now(),
        is_trusted=False,
    )
    
    assert host.host_id == "test-host-123"
    assert host.ip_address == "192.168.1.100"


def test_system_status_model():
    """Test SystemStatus model creation."""
    status = SystemStatus(
        status_id="test-status-123",
        timestamp=datetime.now(),
        cpu_usage=45.5,
        memory_usage=60.2,
        disk_usage=30.1,
        packet_capture_active=True,
        flow_generation_active=False,
        inference_engine_active=True,
        threat_scoring_active=True,
        uptime_seconds=3600,
        total_flows_processed=1000,
        total_threats_detected=5,
    )
    
    assert status.status_id == "test-status-123"
    assert status.cpu_usage == 45.5


def test_model_metadata_model():
    """Test ModelMetadata model creation."""
    metadata = ModelMetadata(
        model_id="test-model-123",
        model_name="lightgbm-traffic-analyzer",
        model_version="1.2.0",
        model_type="LightGBM",
        training_date=datetime.now(),
        feature_count=128,
        accuracy=0.95,
        deployment_environment="production",
    )
    
    assert metadata.model_id == "test-model-123"
    assert metadata.model_name == "lightgbm-traffic-analyzer"


def test_flow_validation():
    """Test that Flow model validation works."""
    # Test valid flow
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
    
    assert flow is not None


if __name__ == "__main__":
    pytest.main([__file__])