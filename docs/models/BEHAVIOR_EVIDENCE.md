# Behavior Evidence Specification

Version: 1.0

Status: Draft

---

# Purpose

Behavior Evidence represents contextual security observations produced by the Behavior Engine.

Unlike machine learning evidence, Behavior Evidence is generated using deterministic rules, historical observations, and behavioural analysis.

It provides context that cannot be inferred from a single network flow.

Behavior Evidence contributes to the Threat Assessment but never directly enforces security policies.

---

# Philosophy

Behavior is evaluated over time.

A single suspicious flow may not indicate malicious intent.

Repeated suspicious behaviour across multiple flows, however, may significantly increase confidence that malicious activity is occurring.

Behavior Evidence provides this temporal context.

---

# Ownership

Produced by:

- Behavior Engine

Consumed by:

- Assessment Engine
- Cloud Policy Engine
- Logger
- Dashboard

---

# Inputs

Behavior Evidence may use:

- Flow
- Feature Vector
- Known Evidence
- Anomaly Evidence
- Historical Host State
- Historical Flow Statistics

The Behavior Engine is responsible for correlating these inputs over configurable time windows.

---

# Lifecycle

Flow

↓

Feature Vector

↓

Known Evidence

+

Anomaly Evidence

↓

Behavior Engine

↓

Behavior Evidence

↓

Threat Assessment

↓

Archive

Behavior Evidence is immutable.

---

# Required Fields

## Metadata

- Evidence ID
- Parent Flow ID
- Timestamp
- Engine Version

---

## Behaviour Summary

- Behaviour Score
- Confidence
- Time Window
- Triggered Rule Count

---

## Triggered Behaviour Rules

Examples include:

- Excessive connection attempts
- Port scanning behaviour
- SSH brute-force pattern
- DNS tunnelling pattern
- Beaconing behaviour
- Excessive failed connections
- Horizontal scanning
- Vertical scanning
- Repeated policy violations

Each triggered rule records:

- Rule Identifier
- Severity
- Description

---

## Historical Context

Optional fields:

- Previous suspicious flows
- Previous blocked attempts
- Historical host reputation
- Recent anomaly count
- Recent known attack count

---

# Validation Rules

A valid Behavior Evidence object shall satisfy:

- Valid Parent Flow ID
- Confidence between 0.0 and 1.0
- Behaviour Score within valid range
- Existing Behaviour Engine version

---

# Explicitly Forbidden

Behavior Evidence shall never contain:

- Firewall actions
- Firewall rules
- Threat Assessment
- Policy Packages
- Executable code
- Shell commands

---

# Relationships

Flow

↓

Known Evidence

+

Anomaly Evidence

↓

Behavior Evidence

↓

Threat Assessment

---

# Serialization

Supported formats:

- JSON
- Pydantic serialization

Future formats:

- MessagePack
- CBOR

---

# Versioning

Every Behavior Evidence object records:

- Schema Version
- Behaviour Engine Version

---

# Performance Requirements

Behaviour analysis shall not delay packet forwarding.

Historical state should be maintained using efficient in-memory data structures.

Expensive computations should be performed asynchronously where possible.

---

# Security

Behaviour rules must be deterministic and explainable.

Every Behaviour Score must be traceable to one or more triggered behaviour rules.

Historical data must never be modified by downstream components.

---

# Definition of Done

The Behavior Evidence specification is complete when:

- Lifecycle is defined.
- Inputs are documented.
- Validation rules are documented.
- Relationships are documented.
- Versioning is documented.
- Performance constraints are documented.
- Security requirements are documented.