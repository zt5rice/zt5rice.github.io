---
title: "GraphAtlas"
category: "GraphRAG · Retrieval engineering"
summary: "A multi-engine knowledge platform with traceable citations and an evaluation harness that makes retrieval quality measurable."
deck: "A knowledge platform that fuses keyword, dense-vector, and graph retrieval, then makes quality and provenance measurable."
boundary: "Portfolio build using a synthetic organizational corpus and a 50-question evaluation set."
problem: "A RAG demo can produce an answer without proving where it came from or whether retrieval improved. GraphAtlas needed citations, graph context, and an evaluation loop that could compare retrieval strategies."
metrics:
  - value: "0.840 Hit@5"
    label: "hybrid retrieval"
  - value: "537 ms p95"
    label: "hybrid latency"
  - value: "4.38 / 5"
    label: "faithfulness"
stack:
  - "PostgreSQL 17"
  - "pgvector"
  - "Hono"
  - "TypeScript"
  - "React"
  - "LightRAG"
repository: "https://github.com/zt5rice/graphatlas"
poster: "/assets/portfolio/projects/graphatlas/graphatlas-demo02-poster.webp"
posterWidth: 1154
posterHeight: 952
order: 2
architecture:
  primary:
    - label: "Documents"
      detail: "PDF, Word, XML, MD, CSV"
    - label: "Parser"
      detail: "normalized source spans"
    - label: "LightRAG"
      detail: "entity + relation extraction"
    - label: "PostgreSQL"
      detail: "pgvector + graph schema"
    - label: "Keyword / Vector / Graph"
      detail: "parallel recall"
    - label: "RRF"
      detail: "rank fusion + router"
    - label: "Agent API"
      detail: "SSE + citations"
  supporting:
    - label: "React graph explorer"
      detail: "one-hop expansion"
    - label: "Benchmark harness"
      detail: "50-question golden set"
  caption: "Synthetic enterprise corpus · traceable evaluation results"
built:
  - "Built local ingestion for PDF, Word, XML, JSON, Markdown, and CSV files, preserving section-level source spans and rejecting failed parses instead of indexing partial documents."
  - "Used a LightRAG-based Python extraction sidecar to create the knowledge graph and load it into PostgreSQL."
  - "Combined PostgreSQL full-text search, pgvector HNSW search, and cycle-safe graph traversal with Reciprocal Rank Fusion."
  - "Served retrieval and streaming answers through a Hono/TypeScript API with a hand-written tool-calling agent and chunk-level citations."
  - "Built a React graph explorer, benchmark dashboard, versioned golden set, four-mode ablation, and traceable result files."
evidence:
  - value: "0.840"
    label: "hybrid Hit@5"
    detail: "Improved from 0.800 with vector-only retrieval on the 50-question set."
    sourceLabel: "GraphAtlas README — measured results"
    sourceUrl: "https://github.com/zt5rice/graphatlas/blob/main/README.md#measured-results-2026-08-22-50-question-golden-set"
  - value: "4.38 / 5"
    label: "faithfulness"
    detail: "LLM-judged answer faithfulness for hybrid retrieval."
    sourceLabel: "GraphAtlas benchmark"
    sourceUrl: "https://github.com/zt5rice/graphatlas/blob/main/docs/BENCHMARK.md"
  - value: "537 ms"
    label: "p95 latency"
    detail: "Measured for hybrid retrieval on the same golden set."
    sourceLabel: "GraphAtlas benchmark"
    sourceUrl: "https://github.com/zt5rice/graphatlas/blob/main/docs/BENCHMARK.md"
media:
  - type: "video"
    src: "/assets/portfolio/projects/graphatlas/media/graphatlas-demo01.mp4"
    poster: "/assets/portfolio/projects/graphatlas/graphatlas-demo01-poster.webp"
    alt: "GraphAtlas document ingestion and job status interface"
    caption: "Document ingestion and graph-build jobs."
    width: 1154
    height: 950
  - type: "video"
    src: "/assets/portfolio/projects/graphatlas/media/graphatlas-demo02.mp4"
    poster: "/assets/portfolio/projects/graphatlas/graphatlas-demo02-poster.webp"
    alt: "GraphAtlas interactive graph explorer with entity and relationship nodes"
    caption: "Interactive graph exploration with one-hop expansion."
    width: 1154
    height: 952
  - type: "video"
    src: "/assets/portfolio/projects/graphatlas/media/graphatlas-demo03.mp4"
    poster: "/assets/portfolio/projects/graphatlas/graphatlas-demo03-poster.webp"
    alt: "GraphAtlas question-answering interface with evidence and tool trace"
    caption: "Question answering with tool trace and chunk-level evidence."
    width: 1154
    height: 952
limitations:
  - "The corpus and organizational entities are synthetic."
  - "The evaluation set is small, uses an LLM judge, and does not establish production traffic performance or multi-tenant security."
sources:
  - label: "Repository"
    url: "https://github.com/zt5rice/graphatlas"
  - label: "Benchmark methodology"
    url: "https://github.com/zt5rice/graphatlas/blob/main/docs/BENCHMARK.md"
  - label: "Architecture and results"
    url: "https://github.com/zt5rice/graphatlas/blob/main/README.md"
---

The useful part is not only that hybrid retrieval scored slightly higher. The system makes the difference inspectable, repeatable, and honest about its limits.
