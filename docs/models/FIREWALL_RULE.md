# Firewall Rule Specification

Version: 1.0

Status: Draft

---

# Purpose

A Firewall Rule represents an executable network filtering rule enforced by the Raspberry Pi.

Firewall Rules are the only objects capable of modifying firewall behavior.

---

# Philosophy

Firewall Rules are implementation objects.

They are not generated directly by machine learning.

They are produced only after validation.

---

# Ownership

Created by:

Rule Engine

Consumed by:

Firewall Manager

---

# Lifecycle

Firewall Decision

↓

Rule Engine

↓

Firewall Rule

↓

Validation

↓

Deployment

↓

Monitoring

↓

Removal

---

# Rule Categories

Static

Created by administrator.

Temporary

Created automatically.

Expires automatically.

Adaptive

Generated from validated Policy Recommendations.

Persistent until removed.

---

# Required Fields

Metadata

- Rule ID
- Creation Timestamp
- Source

Target

- Match Type
- Match Value

Action

- Block
- Allow
- Rate Limit
- Reject

Scope

- Interface
- Direction
- Protocol

Lifetime

- Permanent
- Expiration Time

Status

- Pending
- Active
- Expired
- Disabled

---

# Validation

Every rule must pass:

- Syntax validation
- Conflict detection
- Duplicate detection
- Safety validation

before deployment.

---

# Forbidden

Rules shall never contain:

- Raw AI output
- Shell commands
- Arbitrary scripts

---

# Relationships

Firewall Decision

↓

Firewall Rule

↓

Firewall Manager

---

# Security

Every rule must be reversible.

Every rule must support rollback.

Every deployment must be logged.

---

# Definition of Done

A Firewall Rule is complete when:

- Validation passes
- Deployment succeeds
- Rollback exists