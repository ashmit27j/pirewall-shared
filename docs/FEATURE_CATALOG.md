# Feature Catalog

Version: 1.0

Status: Draft

---

# Purpose

The Feature Catalog defines every feature that may appear in a Feature Vector.

It serves as the authoritative reference for feature extraction, machine learning model training, inference, and future feature engineering.

The Feature Catalog ensures that every component within the Pirewall ecosystem interprets features consistently.

---

# Philosophy

A Flow describes network communication.

A Feature Vector describes numerical representations of that communication.

The Feature Catalog defines what each numerical value represents.

Every feature must have a single authoritative definition.

---

# Ownership

Maintained by:

- Feature Engineering

Used by:

- Feature Extraction Engine
- LightGBM
- Isolation Forest
- Model Training Pipeline
- Model Validation
- Documentation

---

# Feature Categories

Features are grouped into logical categories.

## 1. Flow Metadata

Examples:

- Flow Duration
- Protocol
- Direction

---

## 2. Packet Statistics

Examples:

- Total Packets
- Forward Packets
- Reverse Packets

---

## 3. Byte Statistics

Examples:

- Total Bytes
- Forward Bytes
- Reverse Bytes
- Average Packet Size

---

## 4. Timing Statistics

Examples:

- Packets Per Second
- Bytes Per Second
- Mean Inter-arrival Time
- Standard Deviation of Inter-arrival Time

---

## 5. TCP Features

Examples:

- SYN Count
- ACK Count
- FIN Count
- RST Count
- PSH Count
- URG Count

---

## 6. Connection Behaviour

Examples:

- Connection Rate
- Session Duration
- Failed Connection Count

---

## 7. Statistical Features

Examples:

- Mean Packet Length
- Maximum Packet Length
- Minimum Packet Length
- Packet Length Variance

---

## 8. Derived Features

Examples:

- Forward/Reverse Ratio
- SYN-to-ACK Ratio
- Byte-to-Packet Ratio

Derived features should always be deterministic.

---

# Feature Definition Format

Each feature shall be documented using the following format.

---

## Feature Name

Unique identifier.

Example:

Flow Duration

---

## Description

Clear explanation of the feature.

---

## Data Type

Examples:

- Integer
- Float
- Boolean

---

## Unit

Examples:

- milliseconds
- bytes
- packets
- bytes/second

---

## Valid Range

Minimum and maximum permitted values.

---

## Default Value

Value used if unavailable.

---

## Required

Yes / No

---

## Used By

Examples:

- LightGBM
- Isolation Forest
- Both

---

## Source

Origin of the feature.

Examples:

- Flow Generator
- Feature Extraction Engine

---

## Notes

Additional implementation notes.

---

# Feature Ordering

The order of features within the Feature Vector shall remain stable.

Changing feature order requires:

- Feature Schema Version update
- Model retraining
- Model version increment

---

# Versioning

Every Feature Catalog release shall include:

- Catalog Version
- Feature Schema Version
- Release Date

---

# Validation

Every feature shall satisfy:

- Correct data type
- Valid range
- Deterministic calculation
- Stable definition

---

# Backward Compatibility

New features should be appended whenever possible.

Removing or reordering existing features requires a major schema version.

---

# Performance

Feature extraction should remain lightweight enough for continuous execution on Raspberry Pi hardware.

Expensive calculations should be avoided unless justified by measurable detection improvements.

---

# Security

The Feature Catalog shall never include:

- Raw packet payloads
- Personally identifiable information
- Executable code

Only metadata-derived features are permitted.

---

# Future Extensions

Future feature categories may include:

- TLS metadata
- DNS behaviour
- HTTP metadata
- Flow graph metrics
- Host reputation metrics

These additions shall remain backward compatible whenever possible.