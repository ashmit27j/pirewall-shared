# Threat Assessment Specification

Version: 1.0

Status: Draft

---

# Purpose

Threat Assessment represents the unified security evaluation produced by combining all available evidence sources.

It is the single authoritative description of the security posture of a Flow.

Threat Assessment does not enforce security.

It only evaluates risk.

---

# Philosophy

Threat Assessment combines multiple independent evidence sources into one explainable security assessment.

No single engine determines the outcome.

Every conclusion must be traceable.

---

# Inputs

Known Evidence

+

Anomaly Evidence

+

Behavior Evidence

↓

Threat Assessment

---

# Ownership

Produced by:

Threat Scoring Engine

Consumed by:

Firewall Decision Engine

Cloud

Dashboard

Logger

---

# Lifecycle

Evidence

↓

Threat Assessment Created

↓

Firewall Decision

↓

Archive

Threat Assessment is immutable.

---

# Required Fields

Metadata

- Assessment ID
- Parent Flow ID
- Timestamp

Risk

- Overall Risk Level
- Overall Confidence

Evidence Summary

- Known Evidence Reference
- Anomaly Evidence Reference
- Behavior Evidence Reference

Reasoning

A list of human-readable reasons supporting the assessment.

Example:

- Known SSH brute-force pattern detected
- Host exceeded scan threshold
- High anomaly score observed

Recommendations

Suggested security posture:

- Allow
- Monitor
- Rate Limit
- Temporary Block
- Permanent Block

---

# Explicitly Forbidden

Threat Assessment shall never contain:

- nftables commands
- Shell commands
- Firewall rules
- Cloud responses

Threat Assessment is advisory.

---

# Validation

Confidence:

0.0 ≤ confidence ≤ 1.0

Referenced evidence must exist.

Reason list cannot be empty.

---

# Relationships

Known Evidence

↓

Threat Assessment

Anomaly Evidence

↓

Threat Assessment

Behavior Evidence

↓

Threat Assessment

↓

Firewall Decision

---

# Serialization

JSON

Pydantic

Future:

MessagePack

---

# Security

Every assessment must be explainable.

Every conclusion must reference supporting evidence.

No opaque decisions are permitted.

---

# Versioning

Assessment version

Evidence version

Feature schema version

Model versions

must all be recorded.

---

# Definition of Done

A Threat Assessment is complete when:

- Evidence has been combined.
- Risk has been calculated.
- Confidence has been calculated.
- Reasons have been generated.
- Recommendation has been produced.