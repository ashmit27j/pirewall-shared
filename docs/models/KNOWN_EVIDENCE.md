# Known Evidence Specification

Version: 1.0

Status: Draft

---

# Purpose

Known Evidence represents the output produced by the supervised classification engine.

In Version 1 of Pirewall this engine is LightGBM.

Known Evidence describes how confidently the model believes the observed flow belongs to a previously known attack category.

Known Evidence is not a firewall decision.

---

# Philosophy

Known Evidence represents probability, not certainty.

It contributes evidence to the Threat Assessment.

It never directly blocks traffic.

---

# Ownership

Produced by:

LightGBM Inference Engine

Consumed by:

Threat Assessment Engine

Logging

Cloud

Dashboard

---

# Lifecycle

Feature Vector

↓

LightGBM

↓

Known Evidence

↓

Threat Assessment

Known Evidence is immutable.

---

# Required Fields

Metadata

- Evidence ID
- Parent Flow ID
- Model Version
- Model Name
- Timestamp

Classification

- Predicted Class
- Confidence
- Probability Distribution (optional)

Model Information

- Model Version
- Inference Time
- Feature Schema Version

---

# Validation Rules

Confidence

0.0 ≤ confidence ≤ 1.0

Predicted class must exist in the supported attack taxonomy.

Model version must be known.

Parent Flow ID must exist.

---

# Explicitly Forbidden

Known Evidence shall never contain:

- Threat Score
- Firewall Decision
- Firewall Rule
- Policy Recommendation
- Anomaly Score
- Behavior Score

---

# Relationships

Feature Vector

↓

Known Evidence

↓

Threat Assessment

---

# Versioning

Model version and Feature Schema version shall always be recorded.

---

# Serialization

JSON

Pydantic

Future:

MessagePack

---

# Performance

Inference metadata should remain lightweight.

Large debugging data should never be embedded.

---

# Security

Known Evidence is advisory.

The firewall never trusts a single evidence source.

---

# Definition of Done

The specification is complete when:

- Lifecycle is defined.
- Validation rules are defined.
- Relationships are defined.
- Versioning is documented. 