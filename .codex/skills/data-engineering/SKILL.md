---
name: data-engineering-7ade47
description: Use this skill when the user needs help with data engineering. It provides
  practical guidance, execution steps, and quality checks for data engineering tasks.
keywords:
- database
- schema
- etl
- partition
- indexing
---

# Data Engineering Workflow

## 1. Schema Design
- **Normalization**: Reduce redundancy while maintaining performance.
- **Indexing**: Define primary and composite keys based on access patterns.

## 2. ETL & Processing
- **Extraction**: Efficient fetching from sources.
- **Transformation**: Clean and validate data types.
- **Loading**: Atomic writes to preserve integrity.

## 3. Maintenance Protocols
- **Partioning**: Strategy for handling time-series or high-volume data.
- **Integrity Checks**: Periodic checksums and constraint verification.

## Anti-Patterns
- Storing blobs in relational tables without a storage fallback.
- Design neglect: lack of indexes on high-frequency query columns.
