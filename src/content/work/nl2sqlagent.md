---
title: "NL2SQLAgent"
category: "Governed AI analytics"
summary: "A natural-language interface to a million-row warehouse, designed so generated SQL stays inspectable and read-only."
deck: "A self-service analytics interface that turns natural-language questions into inspectable SQL without allowing generated queries to modify the warehouse."
boundary: "Portfolio build using a seeded synthetic warehouse and a local SQLite database."
problem: "Business users need answers without writing SQL, while engineering still needs guardrails against destructive queries, opaque model behavior, and answers without visible evidence."
metrics:
  - value: "1.03M rows"
    label: "synthetic warehouse"
  - value: "<250 ms"
    label: "query latency"
  - value: "7–15 s"
    label: "LLM inference latency"
stack:
  - "FastAPI"
  - "LangChain"
  - "SQLite"
  - "React"
  - "Server-Sent Events"
  - "ECharts"
repository: "https://github.com/zt5rice/NL2SQLAgent"
poster: "/assets/portfolio/projects/nl2sql/overview.webp"
posterWidth: 1473
posterHeight: 898
order: 3
architecture:
  primary:
    - label: "Question"
      detail: "natural language"
    - label: "Agent"
      detail: "schema inspection"
    - label: "SQL generator"
      detail: "query + explanation"
    - label: "Read-only guard"
      detail: "reject writes before execution"
    - label: "SQLite warehouse"
      detail: "1.03M synthetic rows"
    - label: "Answer + chart"
      detail: "SSE streaming"
  supporting:
    - label: "Session memory"
      detail: "last 10 conversation rounds"
    - label: "ECharts"
      detail: "bar, line, pie, table"
  caption: "Synthetic warehouse · provider-pluggable LLM path"
built:
  - "Built a FastAPI and LangChain query path that inspects the schema, generates SQL, validates it, executes it, and explains the result."
  - "Added defense-in-depth read-only controls that reject write and schema-changing statements before execution."
  - "Streamed thinking, text, SQL, data, chart, and completion events to a React interface over Server-Sent Events."
  - "Built session persistence, context memory, chart heuristics, table and chart views, and deterministic end-to-end checks."
  - "Tested the application against a 1,028,160-row synthetic sales warehouse with indexed query paths."
evidence:
  - value: "1,028,160"
    label: "warehouse rows"
    detail: "Deterministic synthetic sales data seeded locally."
    sourceLabel: "NL2SQLAgent README — performance setup"
    sourceUrl: "https://github.com/zt5rice/NL2SQLAgent/blob/main/README.md#performance"
  - value: "78–235 ms"
    label: "query latency"
    detail: "Measured GROUP BY and date-range queries; documented path stays under 250 ms."
    sourceLabel: "NL2SQLAgent README — performance"
    sourceUrl: "https://github.com/zt5rice/NL2SQLAgent/blob/main/README.md#performance"
  - value: "7–15 s"
    label: "LLM latency"
    detail: "The documented end-to-end bottleneck with the configured deepseek-v4-flash model."
    sourceLabel: "NL2SQLAgent README — performance"
    sourceUrl: "https://github.com/zt5rice/NL2SQLAgent/blob/main/README.md#performance"
media:
  - type: "image"
    src: "/assets/portfolio/projects/nl2sql/overview.webp"
    alt: "NL2SQLAgent interface showing a question, generated SQL, explanation, and revenue chart"
    caption: "The interface exposes the generated SQL and updates the chart while the answer streams in."
    width: 1473
    height: 898
limitations:
  - "The warehouse is synthetic and the local SQLite setup is not a production data platform."
  - "End-to-end latency depends on the configured LLM provider; authentication and multi-tenant authorization are outside this portfolio build."
sources:
  - label: "Repository"
    url: "https://github.com/zt5rice/NL2SQLAgent"
  - label: "Architecture and setup"
    url: "https://github.com/zt5rice/NL2SQLAgent/blob/main/phased_plan_en.md"
  - label: "Performance notes"
    url: "https://github.com/zt5rice/NL2SQLAgent/blob/main/README.md#performance"
---

Natural-language analytics becomes useful only when the generated query is visible, constrained, testable, and tied back to data the user can verify.
