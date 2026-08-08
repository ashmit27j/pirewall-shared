# Anomaly Evidence Specification

Version: 1.0

Status: Draft

---

# Purpose

Anomaly Evidence represents the output produced by the unsupervised anomaly detection engine.

In Version 1 of Pirewall this engine is Isolation Forest.

Unlike Known Evidence, Anomaly Evidence does not classify attacks into predefined categories.

Instead, it estimates how unusual a network flow is when compared to previously observed benign behaviour.

Anomaly Evidence contributes to the Threat Assessment but never makes enforcement decisions.

---

# Philosophy

Anomaly detection complements signature and supervised detection.

Its primary responsibility is identifying:

- Previously unseen attacks
- Zero-day behaviour
- Novel traffic patterns
- Abnormal host behaviour

An anomaly is not automatically malicious.

Every anomaly must be interpreted alongside additional evidence.

---

# Ownership

Produced by:

- Isolation Forest Inference Engine

Consumed by:

- Assessment Engine
- Cloud Policy Engine
- Logger
- Dashboard

---

# Lifecycle

Flow

↓

Feature Extraction

↓

Feature Vector

↓

Isolation Forest

↓

Anomaly Evidence

↓

Threat Assessment

↓

Archive

Anomaly Evidence is immutable.

---

# Required Fields

## Metadata

- Evidence ID
- Parent Flow ID
- Timestamp
- Model Name
- Model Version
- Feature Schema Version

---

## Detection Results

- Anomaly Score
- Normalized Score
- Confidence
- Threshold Used
- Is Anomalous (Boolean)

---

## Model Information

- Training Dataset Version
- Model Checksum
- Inference Time (milliseconds)

---

## Explanation

The engine may optionally provide:

- Most influential features
- Feature importance values
- Distance from learned normal distribution

These explanations are advisory.

---

# Validation Rules

A valid Anomaly Evidence object shall satisfy:

- Parent Flow ID exists
- Confidence is between 0.0 and 1.0
- Normalized Score is between 0.0 and 1.0
- Threshold is valid
- Model version is recognised

---

# Explicitly Forbidden

Anomaly Evidence shall never contain:

- Firewall actions
- Firewall rules
- Threat Assessment
- Policy Packages
- Shell commands
- nftables syntax

---

# Relationships

Flow

↓

Feature Vector

↓

Anomaly Evidence

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

Every Anomaly Evidence object records:

- Schema Version
- Model Version
- Feature Schema Version

Breaking changes require a new major schema version.

---

# Performance Requirements

Inference should be lightweight enough to operate continuously on Raspberry Pi hardware.

Large debugging artefacts must never be embedded in the evidence object.

---

# Security

Anomaly Evidence is advisory.

No firewall action shall be performed solely because an anomaly score exceeds a threshold.

All anomaly detections must be evaluated by the Assessment Engine alongside Known Evidence and Behavior Evidence.

---

# Definition of Done

The Anomaly Evidence specification is complete when:

- Lifecycle is defined.
- Ownership is documented.
- Validation rules are documented.
- Relationships are documented.
- Versioning is documented.
- Serialization is documented.
- Security requirements are documented.