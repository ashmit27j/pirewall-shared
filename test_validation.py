#!/usr/bin/env python3
"""Test validation functionality."""

from datetime import datetime
import sys

try:
    from shared.validation.flow_validator import validate_flow
    from shared.models.flow import Flow
    from shared.enums import ProtocolType, ConnectionState
    
    # Test valid flow validation
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
    
    is_valid = validate_flow(flow)
    print(f"Flow validation result: {is_valid}")
    
    # Test invalid flow (should fail)
    try:
        invalid_flow = Flow(
            source_ip="invalid.ip.address",
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
        print("Invalid flow should have failed validation")
    except Exception as e:
        print(f"Correctly caught invalid flow: {type(e).__name__}")
    
    print("\nValidation tests passed!")
    sys.exit(0)
    
except Exception as e:
    print(f"Validation test failed with error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)