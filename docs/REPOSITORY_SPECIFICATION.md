# Pirewall Shared Repository Specification

Version: 1.0

Status: Draft

---

# Purpose

The `pirewall-shared` repository defines the common language used by every component of the Pirewall ecosystem.

It contains shared domain models, interfaces, schemas, validation logic, events, enumerations, serialization helpers, and common constants.

This repository contains **no business logic**.

It is intended to be imported by:

- pirewall
- pirewall-cloud
- pirewall-dash

Every shared object has exactly one canonical definition inside this repository.

No other repository may redefine shared models.

---

# Repository Goals

The repository shall:

- Provide reusable domain models.
- Ensure type safety.
- Provide validation.
- Provide serialization.
- Define API schemas.
- Define events.
- Define interfaces.
- Maintain backwards compatibility whenever possible.

The repository shall not:

- Capture packets.
- Perform machine learning.
- Execute firewall rules.
- Communicate over the network.
- Connect to databases.
- Contain UI code.

---

# Package Structure

```
shared/

├── models/
├── schemas/
├── interfaces/
├── events/
├── enums/
├── constants/
├── validation/
├── serialization/
├── exceptions/
├── types/
└── version.py
```

---

# Module Responsibilities

## models

Contains immutable domain objects.

Planned models:

- Flow
- ThreatEvidence
- BehaviorEvidence
- ThreatAssessment
- FirewallRule
- PolicyRecommendation
- HostState
- Device
- SystemStatus
- ModelMetadata

Models represent business entities.

Models do not contain business logic.

---

## schemas

Contains API transport models.

Examples:

- HealthResponse
- PolicyRequest
- PolicyResponse
- AuthenticationRequest
- AuthenticationResponse

Schemas exist only for communication.

Schemas are not domain models.

---

## interfaces

Contains abstract interfaces.

Planned interfaces:

- InferenceEngine
- ThreatScorer
- RuleValidator
- BehaviorEngine
- Serializer
- StorageProvider

Interfaces define contracts only.

They contain no implementation.

---

## events

Contains immutable event definitions.

Examples:

- FlowCreated
- ThreatCalculated
- RuleValidated
- RuleApplied
- PolicyReceived
- HostBlocked
- CloudConnected
- CloudDisconnected

Events describe completed actions.

Events never instruct components to perform work.

---

## enums

Contains shared enumerations.

Planned enums:

- Protocol
- ThreatLevel
- ThreatAction
- AttackFamily
- RuleStatus
- PolicyStatus
- ConnectionState
- LogLevel

---

## constants

Contains shared constants.

Examples:

- API versions
- Default thresholds
- Configuration keys
- Timeout values
- Default filenames

Constants must be immutable.

---

## validation

Contains reusable validation logic.

Responsibilities include:

- Model validation
- Schema validation
- Rule validation
- Version compatibility checks

Validation must not modify objects.

---

## serialization

Responsible for converting shared models between supported formats.

Supported formats may include:

- JSON
- YAML
- MessagePack (future)

Serialization must preserve object integrity.

---

## exceptions

Contains custom exception types.

Examples:

- ValidationError
- SerializationError
- VersionMismatchError
- ConfigurationError

Exceptions should communicate meaningful failure reasons.

---

## types

Contains reusable type aliases.

Examples:

- FlowID
- RuleID
- PolicyID
- DeviceID
- ThreatScoreValue

Types improve readability and maintainability.

---

# Dependency Rules

Allowed dependencies:

- models → enums
- models → types
- schemas → models
- validation → models
- serialization → models
- interfaces → models
- events → models

Forbidden dependencies:

- models → schemas
- models → validation
- interfaces → serialization
- interfaces → validation

Circular dependencies are prohibited.

---

# Design Principles

The repository follows these principles:

- Single source of truth.
- Immutable domain models.
- Strong typing.
- Explicit interfaces.
- No duplicated definitions.
- Backward compatibility where practical.
- Separation of domain models and transport schemas.

---

# Coding Standards

Python Version:

Python 3.13+

Libraries:

- Pydantic v2
- typing
- typing_extensions

Mandatory:

- Type hints
- Docstrings
- Unit tests
- Immutable models where applicable

Forbidden:

- Global mutable state
- Wildcard imports
- Business logic
- Networking code

---

# Testing Requirements

Every public object must have tests.

Testing categories:

- Validation tests
- Serialization tests
- Equality tests
- Backward compatibility tests
- Error handling tests

---

# Documentation Requirements

Every public class must include:

- Purpose
- Attributes
- Validation rules
- Usage example

Every module must include:

- Responsibilities
- Dependencies
- Limitations

---

# Versioning

Semantic Versioning (SemVer) shall be used.

Major version:

Breaking changes.

Minor version:

Backward-compatible additions.

Patch version:

Bug fixes.

---

# Future Expansion

Future versions may introduce:

- Additional events.
- New schemas.
- Additional serialization formats.
- Extended validation.
- Additional domain models.

Future additions must preserve repository architecture.

---

# Definition of Done

A component is complete only when:

- Purpose is documented.
- Public API is defined.
- Type hints exist.
- Validation exists.
- Serialization exists.
- Tests pass.
- Documentation is complete.
- Architecture rules are respected.

---

# Current Status

The repository is currently in the Specification Phase.

No implementation shall begin until:

- Domain models are fully specified.
- Interfaces are finalized.
- Events are finalized.
- Validation strategy is approved.