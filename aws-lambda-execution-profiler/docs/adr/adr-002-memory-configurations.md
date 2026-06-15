# ADR 002 — Memory Configurations to Test

## Status
Accepted

## Context
AWS Lambda supports memory sizes from 128 MB to 10,240 MB. Testing every possible memory tier is unnecessary, time-consuming, and expensive. The goal is to test a representative set that demonstrates performance scaling while keeping costs low.

## Decision
Test the following memory configurations:
- 128 MB
- 256 MB
- 512 MB
- 1024 MB

## Rationale
- Covers low, medium, and high memory tiers
- Matches common AWS Power Tuning defaults
- Provides enough data to understand CPU scaling
- Keeps profiling cost reasonable

## Alternatives Considered
- Test all memory sizes from 128 MB to 10 GB
- Test only 128 MB and 1024 MB
- Dynamically choose memory sizes based on previous results

## Consequences
- Produces meaningful results without excessive cost
- Additional tiers can be added later if needed
- May miss edge cases at very high memory sizes
