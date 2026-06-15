# ADR 003 — Storing Profiling Results in JSON Format

## Status
Accepted

## Context
The Lambda Power Tuning workflow outputs structured data including execution time, cost per invocation, visualization metadata, and the recommended memory configuration. This data must be stored in a format that is easy to parse, version, and visualize.

## Decision
Store raw profiling results in JSON format under:
```code
docs/profiling-results/raw-results.json
```

## Rationale
- JSON is the native output format of Step Functions
- Easy to use in scripts, dashboards, or visualizers
- Works well with GitHub version control
- Human-readable and machine-readable

## Alternatives Considered
- Store results in CSV
- Store results in DynamoDB
- Store results only as Markdown tables

## Consequences
- No additional transformation required
- Developers can build custom visualizations easily
- JSON must be manually interpreted unless paired with a chart
