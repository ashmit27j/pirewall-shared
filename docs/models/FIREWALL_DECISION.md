# Firewall Decision Specification

Version: 1.0

Status: Draft

---

# Purpose

A Firewall Decision represents the final enforcement decision for a single Flow.

It is produced by the Decision Engine using the Threat Assessment and the current security policy.

The Firewall Decision is the only object that may instruct the Firewall Manager to take action.

---

# Philosophy

Threat Assessment answers:

"How dangerous is this?"

Firewall Decision answers:

"What should the firewall do?"

The same Threat Assessment may produce different Firewall Decisions depending on deployment policy.

---

# Ownership

Produced by:

Decision Engine

Consumed by:

- Firewall Manager
- Cloud Synchronization
- Logger
- Dashboard

---

# Lifecycle

Threat Assessment

↓

Decision Engine

↓

Firewall Decision

↓

Firewall Manager

↓

Archive

Firewall Decisions are immutable.

---

# Required Fields

Metadata

- Decision ID
- Parent Flow ID
- Timestamp

Decision

- Action
- Priority
- Duration (if temporary)
- Reason

Policy

- Policy Version
- Policy Name

Evidence

- Threat Assessment ID

---

# Supported Actions

The supported actions are:

- Allow
- Monitor
- Alert
- Rate Limit
- Temporary Block
- Permanent Block

Future actions may be added in a backward-compatible manner.

---

# Explicitly Forbidden

A Firewall Decision shall never contain:

- nftables commands
- Shell commands
- Raw packets
- ML predictions
- Feature vectors

It specifies intent, not implementation.

---

# Validation Rules

A valid Firewall Decision shall satisfy:

- Supported action
- Valid priority
- Existing Threat Assessment reference
- Existing policy version
- Non-empty reason

Temporary Block actions must include a duration.

Permanent Block actions must not include a duration.

---

# Relationships

Threat Assessment

↓

Firewall Decision

↓

Firewall Manager

↓

Firewall Rule (optional)

---

# Serialization

Supported formats:

- JSON
- Pydantic serialization

---

# Security

Every Firewall Decision must be explainable.

Every decision must reference:

- The Threat Assessment
- The policy used
- The reasoning

No enforcement action may occur without a valid Firewall Decision.

---

# Versioning

Every decision records:

- Decision schema version
- Policy version
- Threat Assessment version

---

# Definition of Done

The Firewall Decision specification is complete when:

- Lifecycle is defined.
- Actions are defined.
- Validation rules are documented.
- Relationships are documented.
- Security requirements are documented.