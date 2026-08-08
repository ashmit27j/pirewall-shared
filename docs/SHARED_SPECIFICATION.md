\# Pirewall Shared Specification



Version: 1.0



Status: Draft



\---



\# Purpose



This document defines the shared domain model architecture for the entire Pirewall ecosystem.



The repository serves as the canonical source of truth for all shared objects exchanged between the Raspberry Pi firewall, the cloud services, and the dashboard.



Every shared object is specified before implementation.



No implementation should begin until its specification has been approved.



\---



\# Design Philosophy



Shared models are:



\- Immutable where practical.

\- Strongly typed.

\- Versioned.

\- Serializable.

\- Independently testable.

\- Free of business logic.



Models describe data.



Behavior belongs elsewhere.



\---



\# Domain Model Categories



The shared library contains five categories of objects.



\## 1. Domain Models



Business entities used throughout the system.



Examples:



\- Flow

\- ThreatAssessment

\- FirewallRule



\---



\## 2. Transport Schemas



Objects used only for communication.



Examples:



\- API requests

\- API responses



\---



\## 3. Events



Immutable records describing completed actions.



Examples:



\- FlowCreated

\- RuleApplied



\---



\## 4. Interfaces



Abstract contracts implemented by consuming repositories.



\---



\## 5. Supporting Types



Enums, constants, aliases, and exceptions.



\---



\# Canonical Domain Models



The following models form the backbone of Pirewall.



1\. Flow

2\. ThreatEvidence

3\. BehaviorEvidence

4\. ThreatAssessment

5\. FirewallRule

6\. PolicyRecommendation

7\. HostState

8\. SystemStatus

9\. ModelMetadata



Each model has its own specification document.



\---



\# Specification Rules



Every model specification must define:



\- Purpose

\- Ownership

\- Lifecycle

\- Immutability

\- Relationships

\- Fields

\- Validation Rules

\- Serialization

\- Versioning

\- Usage Examples

\- Future Extension Points



No implementation details belong in these specifications.



\---



\# Document Index



| Model | Specification |

|--------|---------------|

| Flow | models/FLOW.md |

| ThreatEvidence | models/THREAT\_EVIDENCE.md |

| BehaviorEvidence | models/BEHAVIOR\_EVIDENCE.md |

| ThreatAssessment | models/THREAT\_ASSESSMENT.md |

| FirewallRule | models/FIREWALL\_RULE.md |

| PolicyRecommendation | models/POLICY\_RECOMMENDATION.md |

| HostState | models/HOST\_STATE.md |

| SystemStatus | models/SYSTEM\_STATUS.md |

| ModelMetadata | models/MODEL\_METADATA.md |



\---



\# Development Process



For each model:



1\. Write the specification.

2\. Review and approve.

3\. Implement the model.

4\. Add validation.

5\. Add serialization.

6\. Add tests.

7\. Freeze the public API.



No implementation may skip the specification phase.

