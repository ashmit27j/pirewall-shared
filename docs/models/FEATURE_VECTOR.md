# Feature Vector Specification

Version: 1.0

Status: Draft

---

# Purpose

The Feature Vector represents the numerical features extracted from a Flow for use by machine learning models and analytical components.

It is the canonical input to all detection engines.

A Feature Vector is derived from exactly one Flow.

It contains no security decisions.

---

# Philosophy

The Feature Vector separates network representation from machine learning representation.

A Flow describes network communication.

A Feature Vector describes measurable characteristics of that communication.

This separation allows feature engineering without changing the Flow model.

---

# Ownership

Created by:

Feature Extraction Engine

Consumed by:

- LightGBM
- Isolation Forest
- Behavior Engine (optional)
- Future detection engines

---

# Lifecycle

Flow
↓

Feature Extraction

↓

Feature Vector Created

↓

Inference

↓

Archived

The Feature Vector is immutable after creation.

---

# Identity

Each Feature Vector contains:

- Feature Vector ID
- Parent Flow ID
- Schema Version

---

# Required Fields

## Metadata

- Feature Vector ID
- Parent Flow ID
- Feature Schema Version
- Creation Timestamp

---

## Features

The vector contains only numerical or encoded values suitable for computation.

Feature names and ordering are defined by the Feature Schema.

Examples include:

- Flow duration
- Total packets
- Total bytes
- Forward packet count
- Reverse packet count
- Average packet size
- Bytes per second
- Packets per second
- TCP flag counts
- Inter-arrival statistics

The exact feature list is intentionally maintained separately from this specification.

---

# Explicitly Forbidden

The Feature Vector must never contain:

- Threat scores
- ML predictions
- Firewall actions
- Policy recommendations
- Raw packets
- Payload data
- Behavioral decisions

---

# Validation Rules

A valid Feature Vector shall satisfy:

- Valid parent Flow ID
- Supported schema version
- Correct feature count
- Correct feature ordering
- Numeric feature values
- No missing required features

---

# Serialization

Supported formats:

- JSON
- Pydantic serialization

Future support:

- MessagePack
- CBOR

---

# Relationships

Flow

↓

Feature Vector

↓

Known Evidence

↓

Anomaly Evidence

↓

Behavior Evidence

The Feature Vector does not reference downstream objects.

---

# Versioning

Every Feature Vector references a Feature Schema version.

Feature extraction and inference must use compatible schema versions.

---

# Performance Requirements

Feature Vectors should be compact.

Duplicate information already present in the Flow should be avoided where practical.

---

# Security Considerations

Feature Vectors contain derived network metadata.

They contain no payload data.

---

# Definition of Done

The Feature Vector specification is complete when:

- Ownership is defined.
- Lifecycle is defined.
- Validation rules are documented.
- Serialization is documented.
- Relationships are documented.
- Versioning is defined.