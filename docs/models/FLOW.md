# Flow Specification

Version: 1.0

Status: Draft

---

# Purpose

The Flow is the canonical network observation object used throughout the Pirewall ecosystem.

It represents a completed or expired network communication aggregated from one or more packets.

The Flow replaces raw packets as soon as packet capture and aggregation are complete.

No downstream component shall consume raw packets.

---

# Philosophy

The Flow is designed to be:

- Immutable after creation.
- Lightweight.
- Serializable.
- Versioned.
- Independent of packet capture implementation.
- Independent of machine learning implementation.

The Flow describes network behavior.

It does not describe security decisions.

---

# Ownership

Created by:

Flow Generator

Consumed by:

- Feature Extraction
- LightGBM
- Isolation Forest
- Behavior Engine
- Threat Scoring
- Logger
- Cloud Client
- Dashboard APIs

---

# Lifecycle

```

Packet
↓
Packet Capture
↓
Flow Generator
↓
Flow Object Created
↓
Feature Extraction
↓
Inference
↓
Threat Assessment
↓
Archive

```

A Flow is never modified after creation.

Derived information is stored separately.

---

# Identity

Each Flow has one globally unique identifier.

The identifier must remain constant throughout the Flow's lifetime.

The identifier must never depend on memory addresses or runtime state.

---

# Required Fields

## Identification

- Flow ID
- Flow Version

---

## Network

- Source IP
- Destination IP
- Source Port
- Destination Port
- Protocol

---

## Timing

- Start Timestamp
- End Timestamp
- Duration

---

## Volume

- Total Packets
- Total Bytes
- Forward Packets
- Reverse Packets
- Forward Bytes
- Reverse Bytes

---

## Transport

- TCP Flags Summary
- Connection State

---

## Feature Vector

The Flow stores the extracted numerical feature vector.

The exact feature list is defined independently from the Flow model.

This allows feature engineering without redesigning the Flow.

---

## Metadata

Optional metadata may include:

- Interface Name
- VLAN ID
- Capture Source
- Sensor Identifier

Metadata is informational only.

---

# Explicitly Forbidden

The Flow must never contain:

- ML predictions
- Threat scores
- Firewall actions
- Policy recommendations
- Behavioral scores
- Rule IDs
- Dashboard state
- UI information

These belong to downstream models.

---

# Immutability

After creation:

No field may be modified.

Any derived analysis must produce a new object.

Example:

Flow

↓

ThreatEvidence

↓

ThreatAssessment

The original Flow remains unchanged.

---

# Validation Rules

A valid Flow shall satisfy:

- Valid IP addresses
- Supported protocol
- Non-negative ports
- End time >= Start time
- Packet count >= 1
- Byte count >= 0
- Valid identifier
- Valid feature vector length

Invalid Flows shall be rejected.

---

# Serialization

The Flow must support:

- JSON
- Pydantic serialization

Future support may include:

- MessagePack
- CBOR

Serialization must preserve all values exactly.

---

# Versioning

Every Flow contains a schema version.

Breaking structural changes require a new major version.

Consumers must reject unsupported versions.

---

# Relationships

The Flow is the parent object for:

- ThreatEvidence
- BehaviorEvidence
- ThreatAssessment

These objects reference the Flow.

The Flow never references them.

Dependency direction always points away from the Flow.

---

# Performance Requirements

The Flow should remain compact enough to minimize memory usage and serialization overhead.

Repeated or derived information should not be duplicated unnecessarily.

---

# Security Considerations

The Flow contains operational network metadata.

Sensitive information should be handled according to deployment requirements.

The Flow must not contain payload data.

Payload inspection is outside the scope of Pirewall Version 1.

---

# Extension Policy

New fields may be added only if they:

- are generally useful,
- are independent of specific ML models,
- preserve backward compatibility where possible,
- do not violate immutability.

Fields specific to one detection algorithm belong outside the Flow.

---

# Definition of Done

The Flow specification is complete when:

- Lifecycle is defined.
- Ownership is defined.
- Required fields are finalized.
- Validation rules are documented.
- Serialization rules are documented.
- Versioning strategy is documented.
- Relationships are documented.
- Performance constraints are documented.

Only then may implementation begin.