# Portfolio Content and Fact Sheet

Approved direction: `Software Engineer · Data & AI Systems`

Language: English-first

This file is the source of truth for website copy. Implementation should use the
approved strings below rather than inventing new claims. Every quantitative claim
must remain traceable to the evidence register in this document.

## Identity and metadata

### Site title

`Dr. Zhao Tang — Software Engineer, Data & AI Systems`

### Meta description

`Zhao Tang builds reliable data platforms, measurable AI products, and production systems. Explore selected work across streaming data, GraphRAG, natural-language analytics, and scientific computing.`

### Open Graph title

`Zhao Tang — Data & AI Systems`

### Open Graph description

`Reliable data platforms, measurable AI products, and production systems built to hold up under real load.`

### Public contact details

- Location: `San Diego, California`
- Email: `ztangintuit@gmail.com`
- LinkedIn: `https://www.linkedin.com/in/tzhao7-sde/`
- GitHub: `https://github.com/zt5rice`
- Website: `https://zt5rice.github.io/`
- Phone: do not publish

## Navigation and global labels

### Primary navigation

- `Work`
- `Experience`
- `About`
- `Research`
- `Contact`

### Global calls to action

- Primary: `Explore selected work`
- Resume: `Download resume`
- Project: `Read case study`
- Repository: `View on GitHub`
- Email: `Email me`

## Homepage copy

### Hero

Eyebrow:

`SAN DIEGO, CALIFORNIA`

Name:

`Dr. Zhao Tang`

Discipline:

`Software Engineer · Data & AI Systems`

Value proposition:

`I build reliable data platforms, measurable AI products, and production systems that hold up under real load.`

Supporting paragraph:

`From real-time pipelines and retrieval evaluation to on-call reliability, I work across the system—not just the model or the dashboard.`

Primary CTA:

`Explore selected work`

Secondary CTA:

`Download resume`

### Proof strip

| Value | Label |
| --- | --- |
| `100M+` | TurboTax and QuickBooks users supported by Intuit data products |
| `40%` | Lower MTTR through distributed tracing and root-cause analysis |
| `0.840` | Hybrid Hit@5 on GraphAtlas's 50-question benchmark |
| `6` | Peer-reviewed publications, plus conference posters and presentations |

### Selected work introduction

Section label:

`SELECTED WORK`

Heading:

`Systems built for evidence, not just demos.`

Introduction:

`The portfolio spans streaming infrastructure, retrieval engineering, governed analytics, and scientific computing. Each case study includes the architecture, measured outcomes, and the boundary between a portfolio build and production traffic.`

### Project cards

#### Clickstream

Label:

`STREAMING DATA PLATFORM`

Title:

`Clickstream`

Summary:

`An end-to-end streaming platform that turns high-volume events into monitored, queryable data products.`

Visible metrics:

- `~100 events/s`
- `p95 181 ms`
- `111 tests`

Stack line:

`Python · Kafka · Spark · PostgreSQL · ClickHouse · FastAPI`

Boundary:

`Portfolio system · synthetic traffic`

#### GraphAtlas

Label:

`GRAPH RAG · RETRIEVAL ENGINEERING`

Title:

`GraphAtlas`

Summary:

`A multi-engine knowledge platform with traceable citations and an evaluation harness that makes retrieval quality measurable.`

Visible metrics:

- `0.840 Hit@5`
- `537 ms p95`
- `4.38 / 5 faithfulness`

Stack line:

`PostgreSQL + pgvector · Hono · TypeScript · React · LightRAG`

Boundary:

`Portfolio system · synthetic corpus`

#### NL2SQLAgent

Label:

`GOVERNED AI ANALYTICS`

Title:

`NL2SQLAgent`

Summary:

`A natural-language interface to a million-row warehouse, designed so generated SQL stays inspectable and read-only.`

Visible metrics:

- `1.03M rows`
- `<250 ms queries`
- `7–15 s LLM latency`

Stack line:

`FastAPI · LangChain · SQLite · React · Server-Sent Events`

Boundary:

`Portfolio system · synthetic warehouse`

#### nanotrack

Label:

`RESEARCH DATA INFRASTRUCTURE`

Title:

`nanotrack`

Summary:

`A scientific video-tracking pipeline rebuilt from MATLAB into a reproducible Python system with orchestration, observability, and CI.`

Visible metrics:

- `15 h → 30 min`
- `6 papers`
- `10k-frame run`

Stack line:

`Python · Dask · OpenCV · FastAPI · Airflow · Prometheus · Grafana`

Boundary:

`Research software · synthetic and real-data support`

## Case-study copy

### Clickstream

Category:

`Real-time data platform`

Deck:

`A production-shaped clickstream pipeline built to test the full path from event generation to a monitored read API.`

Boundary:

`Portfolio build using synthetic events and short-run local or kind-cluster measurements. Not an employer production system.`

#### Problem

`Streaming projects often stop at a dashboard. The harder question is whether the event contract, state model, query layer, and failure paths hold together when data is late, duplicated, malformed, or temporarily unavailable.`

#### What I built

- `Built a deterministic producer and Kafka ingestion path, then processed one-minute windows in Spark Structured Streaming with watermarking and a dead-letter topic.`
- `Modeled curated data for PostgreSQL and analytical data for ClickHouse, with idempotent upserts and a read-only FastAPI serving layer.`
- `Added Airflow orchestration, dbt models and tests, data-quality checks, Redis caching, rate limiting, and a Go operations CLI.`
- `Instrumented the system with Prometheus and Grafana, then added SLOs, runbooks, k6 load tests, and chaos drills.`
- `Deployed through Docker Compose and kind/Helm, with a time-boxed Terraform/EKS run that was destroyed in the same session.`

#### Evidence

- `~100 events/s steady-state producer with zero failed events in the recorded run.`
- `46 requests/s at p95 180.6 ms with 0% errors in the k6 test.`
- `111 Python tests passing, 15 dbt tests passing, and 11 data-quality checks passing.`
- `API and Kafka pod-recovery drills measured 21 s and 33 s MTTR respectively.`
- `The time-boxed EKS verification cost less than $2 and was torn down immediately.`

#### Trade-offs and limitations

`The system uses synthetic events, a short measurement window, and a single-node Kafka configuration. It demonstrates production-shaped engineering, not production traffic, multi-region resilience, or a long-running SLO history.`

#### Takeaway

`I treated observability, data quality, failure recovery, and cost control as part of the pipeline—not as follow-up work.`

### GraphAtlas

Category:

`Multi-engine GraphRAG platform`

Deck:

`A knowledge platform that fuses keyword, dense-vector, and graph retrieval, then makes quality and provenance measurable.`

Boundary:

`Portfolio build using a synthetic organizational corpus and a 50-question evaluation set.`

#### Problem

`A RAG demo can produce an answer without proving where it came from or whether retrieval improved. GraphAtlas needed citations, graph context, and an evaluation loop that could compare retrieval strategies.`

#### What I built

- `Built local ingestion for PDF, Word, XML, JSON, Markdown, and CSV files, preserving section-level source spans and rejecting failed parses instead of indexing partial documents.`
- `Used a LightRAG-based Python extraction sidecar to create the knowledge graph and load it into PostgreSQL.`
- `Combined PostgreSQL full-text search, pgvector HNSW search, and cycle-safe graph traversal with Reciprocal Rank Fusion.`
- `Served retrieval and streaming answers through a Hono/TypeScript API with a hand-written tool-calling agent and chunk-level citations.`
- `Built a React graph explorer, benchmark dashboard, versioned golden set, four-mode ablation, and traceable result files.`

#### Evidence

- `50-question golden set with four retrieval modes.`
- `Hybrid Hit@5: 0.840 versus 0.800 for vector-only.`
- `Faithfulness: 4.38 / 5.`
- `Hybrid p95 latency: 537 ms.`
- `Every reported metric traces to JSON under benchmark/results/.`

#### Trade-offs and limitations

`The corpus and organizational entities are synthetic. The evaluation set is small, uses an LLM judge, and does not establish production traffic performance, multi-tenant security, or long-running operational reliability.`

#### Takeaway

`The useful part is not that hybrid retrieval scored slightly higher. It is that the system makes the difference inspectable, repeatable, and honest about its limits.`

### NL2SQLAgent

Category:

`Governed natural-language analytics`

Deck:

`A self-service analytics interface that turns natural-language questions into inspectable SQL without allowing generated queries to modify the warehouse.`

Boundary:

`Portfolio build using a seeded synthetic warehouse and a local SQLite database.`

#### Problem

`Business users need answers without writing SQL, while engineering still needs guardrails against destructive queries, opaque model behavior, and answers without visible evidence.`

#### What I built

- `Built a FastAPI and LangChain query path that inspects the schema, generates SQL, validates it, executes it, and explains the result.`
- `Added defense-in-depth read-only controls that reject write and schema-changing statements before execution.`
- `Streamed thinking, text, SQL, data, chart, and completion events to a React interface over Server-Sent Events.`
- `Built session persistence, context memory, chart heuristics, table and chart views, and deterministic end-to-end checks.`
- `Tested the application against a 1,028,160-row synthetic sales warehouse with indexed query paths.`

#### Evidence

- `1,028,160 rows in the seeded sales table.`
- `Measured GROUP BY and date-range queries between 78 ms and 235 ms; the documented query path stays under 250 ms.`
- `The documented end-to-end bottleneck is 7–15 s of LLM inference latency, rather than the local query path.`

#### Trade-offs and limitations

`The warehouse is synthetic, the local SQLite setup is not a production data platform, and end-to-end latency depends on the configured LLM provider. Authentication, multi-tenant authorization, and enterprise SQL governance are outside this portfolio build.`

#### Takeaway

`Natural-language analytics becomes useful only when the generated query is visible, constrained, testable, and tied back to the data the user can verify.`

### nanotrack

Category:

`Scientific computing and research data infrastructure`

Deck:

`A single-molecule video-tracking pipeline rebuilt from MATLAB into a reproducible Python system with serving, orchestration, observability, and CI.`

Boundary:

`Research software. The original methodology supports published work; the open-source Python pipeline is a 2026 engineering reimplementation.`

#### Problem

`Scientific video analysis was trapped in a research workflow that was difficult to reproduce, parallelize, monitor, and hand to another engineer.`

#### What I built

- `Reimplemented detection, tracking, orientation unwrapping, feature extraction, and validation in a Python package.`
- `Added interchangeable NumPy, OpenCV, and scikit-image preprocessing backends.`
- `Parallelized chunked processing with Dask and documented a SLURM path for long cluster runs.`
- `Built a FastAPI service, Airflow DAG, Docker Compose stack, Prometheus metrics, and a provisioned Grafana dashboard.`
- `Added immutable run artifacts, checkpoint resume, self-contained QC reports, tracking overlays, and GitHub Actions CI.`

#### Evidence

- `Per-experiment processing time reduced from 15 hours to 30 minutes in the original cluster workflow.`
- `Methods and datasets support 6 peer-reviewed publications, plus additional conference posters and presentations.`
- `Generated and validated a 10,000-frame synthetic single-molecule run with anisotropic diffusion.`
- `Automated validation reached greater than 99% data consistency in the research workflow.`

#### Trade-offs and limitations

`Synthetic data is the default demo path; real TIFF and ND2 loaders exist but are not part of every CI run. The Python package is an engineering reimplementation, not a claim that every historical publication was produced with this exact codebase.`

#### Takeaway

`The research background shaped how I build software: preserve provenance, make the measurement repeatable, and design for the next person who has to run it.`

## Experience

### Section introduction

Label:

`EXPERIENCE`

Heading:

`Where data correctness meets system reliability.`

Introduction:

`I have worked across real-time data platforms, customer-facing measurement, production incident response, and research software. The common thread is making complex systems observable, reproducible, and useful to the people who depend on them.`

### Intuit — Software Engineer, Customer Product & Experience Optimization

Date:

`07/2025 — 07/2026`

Context:

`Intuit · Customer Product Organization · TurboTax`

Summary:

`Owned production data quality and measurement for TurboTax while serving as primary on-call engineer.`

Bullets:

- `Cut MTTR by 40% by using distributed tracing and root-cause analysis, with durable corrective actions and runbooks.`
- `Led a cross-organization remediation of millions of missing records and aligned three organizations on one metric definition and validation standard.`
- `Raised experiment device coverage by 10+ percentage points, moving from the mid-60s to the high-70s.`
- `Upgraded batch pipelines to incremental processing, reducing peak processing time from 7 hours to 15 minutes and peak infrastructure cost by 95%.`
- `Built validation and monitoring that surfaced incorrect data before it reached reporting.`

### Intuit — Software Engineer, Data Platform & Analytics Infrastructure

Date:

`03/2024 — 07/2025`

Context:

`Intuit · Analytics, AI & Data · TurboTax and QuickBooks`

Summary:

`Built real-time data platforms and foundational datasets for products used by more than 100 million people.`

Bullets:

- `Built real-time pipelines and datasets powering daily decisions for 100M+ TurboTax and QuickBooks users.`
- `Mapped dependencies across 100+ pipelines and approximately 1,000 tables, cutting manual cross-team approval coordination by about 50%.`
- `Fixed a multi-year stateful defect, restoring cumulative tracking since 2020 for 10M+ unique visitors and 1M+ daily sessions.`
- `Created operational and analytical datasets from scratch and partnered with product, analytics, and data teams on definitions and validation.`

### Rice University — Research Specialist, Research Data Infrastructure

Date:

`06/2023 — 03/2024`

Context:

`Rice University · George R. Brown School of Engineering and Computing`

Summary:

`Engineered reproducible data infrastructure for multi-terabyte scientific datasets.`

Bullets:

- `Built Python workflows with automated validation and greater than 99% data consistency for scientific users.`
- `Parallelized multi-terabyte video and unstructured-data processing on HPC clusters.`
- `Re-engineered a MATLAB tracking methodology into the open-source nanotrack Python pipeline.`

### Rice University — Visiting Scholar, Computational Imaging & Machine Learning

Date:

`05/2022 — 05/2023`

Context:

`Rice University · Chemical and Biomolecular Engineering`

Summary:

`Built computational-imaging and machine-learning pipelines for single-molecule and nanoparticle analysis.`

Bullets:

- `Developed automated image-processing and optical-analysis software in Python and MATLAB.`
- `Reduced per-experiment processing time from 15 hours to 30 minutes through cluster parallelization.`
- `Published methods and datasets that support 6 peer-reviewed papers, with additional conference posters and presentations.`

## About

Section label:

`ABOUT`

Heading:

`I care about the part after the demo works.`

Paragraphs:

`Science taught me to treat measurement as part of the system. Industry taught me that correctness only matters if it survives real traffic, changing schemas, ambiguous definitions, and the person who gets paged at 2 a.m.`

`I started in computational imaging and completed a PhD at Rice, building software to extract measurable signals from complex scientific data. At Intuit, I moved into real-time data platforms and customer-facing data products: defining data-quality metrics, stabilizing stateful pipelines, tracing production failures, and aligning teams on one definition of truth.`

`Today I focus on systems where data, AI, and reliability meet: streaming pipelines, retrieval and evaluation, governed natural-language analytics, and the observability that keeps them operable.`

### Current focus

- `Reliable data platforms`
- `Retrieval and evaluation for AI systems`
- `Production observability`
- `Scientific computing`

### Education

- `PhD, Chemical & Biomolecular Engineering — Rice University`
- `MS, Computer Science — Georgia Institute of Technology (in progress)`
- `DBA, Business Analytics — Westcliff University (in progress)`
- `BS, Chemical Engineering — Purdue University`

## Technical toolkit

### Data and streaming

`Python · SQL · Spark · Kafka · Airflow · dbt · Databricks · Delta Lake · PostgreSQL · ClickHouse · Redis`

### Cloud and reliability

`AWS · Docker · Kubernetes · Helm · Terraform · GitHub Actions · Prometheus · Grafana · Linux`

### Backend and APIs

`FastAPI · REST · Server-Sent Events · TypeScript · Hono`

### AI and retrieval

`pgvector · RAG / GraphRAG · Reciprocal Rank Fusion · LLM evaluation · LangChain`

### Languages

`Python · SQL · Scala · Go · TypeScript / JavaScript · Bash`

## Research

Section label:

`RESEARCH`

Heading:

`Measurement, reproducibility, and scientific computing.`

Copy:

`My research background spans computational imaging, single-molecule tracking, machine learning, and research data infrastructure. The work produced 6 peer-reviewed publications, along with conference posters and presentations, and taught me to preserve provenance, validate methods, and make complex results reproducible.`

Research record:

`View research record`

URL:

`https://scholar.google.com/citations?user=WlAErpUAAAAJ&hl=en`

Closing copy:

`The research track is not separate from the engineering story. It is why I care about trustworthy metrics, clear evidence, and systems that another person can reproduce.`

## Contact

Section label:

`CONTACT`

Heading:

`Let’s build systems that can be trusted after launch.`

Copy:

`For roles, collaborations, or technical conversations about data platforms, production AI, and reliability, reach me at the links below.`

Calls to action:

- `Email me`
- `LinkedIn`
- `GitHub`
- `Download resume`

## Footer

`Designed and built by Zhao Tang · San Diego, California`

## Fact register

Every public metric below has an exact source. If implementation needs a new
number, add it here first with evidence.

| ID | Public claim | Exact value | Evidence |
| --- | --- | --- | --- |
| F01 | Intuit scale | `100M+` TurboTax and QuickBooks users | `Resume/Zhao_Tang_Resume_DataEngineer_2026-10-19.docx`, Summary and Intuit Data Platform role |
| F02 | Reliability improvement | `40%` MTTR reduction | Data Engineer resume, Customer Product role; ResMed resume, Reliability & System Health |
| F03 | Experiment coverage | `10+` percentage points; mid-60s to high-70s | Data Engineer resume, Customer Product role |
| F04 | Cross-org remediation | millions of missing records; three organizations | Data Engineer resume, Customer Product role |
| F05 | Lineage scale | `100+` pipelines; approximately `1,000` tables; `~50%` less manual coordination | Data Engineer resume, Data Platform role |
| F06 | Stateful data repair | tracking since 2020; `10M+` unique visitors; `1M+` daily sessions | Data Engineer resume, Data Platform role |
| F07 | Batch improvement | `7 h → 15 min`; `95%` lower peak infrastructure cost | ResMed resume, Performance & Cost |
| F08 | Publications | `6` peer-reviewed publications; additional conference posters/presentations | Google Scholar profile: `https://scholar.google.com/citations?user=WlAErpUAAAAJ&hl=en` |
| F09 | Research consistency | greater than `99%` data consistency | Data Engineer resume, Research Specialist role |
| F10 | Research speedup | `15 h → 30 min` per experiment | Nanoparticle README; both resumes |
| F11 | Clickstream producer | `~100` events/s; `0` failed events in recorded run | `/Users/zhaotang/projects/clickstream/README.md`, Phase 1 metrics |
| F12 | Clickstream load | `46` req/s; p95 `180.6 ms`; `0%` errors | `clickstream/README.md`, Phase 4 metrics; `DESIGN.md` |
| F13 | Clickstream engineering tests | `111` Python tests; `15/15` dbt tests; `11/11` quality checks | `clickstream/README.md`, Phases 2 and 4 |
| F14 | Clickstream chaos recovery | API `21 s`; Kafka `33 s` MTTR | `clickstream/README.md`, Phase 4; `DESIGN.md` |
| F15 | Clickstream EKS cost | less than `$2` for the time-boxed run | `clickstream/README.md`, Phase 3; ResMed resume |
| F16 | GraphAtlas evaluation set | `50` questions; `4` retrieval modes | `knowledgeRAG/README.md`; `docs/BENCHMARK.md` |
| F17 | GraphAtlas retrieval quality | hybrid Hit@5 `0.840`; vector-only `0.800` | `knowledgeRAG/README.md`; `benchmark/results/2026-08-22-hybrid.json` |
| F18 | GraphAtlas faithfulness | `4.38 / 5` hybrid | `knowledgeRAG/README.md`; benchmark results JSON |
| F19 | GraphAtlas latency | hybrid p95 `537 ms` | `knowledgeRAG/docs/BENCHMARK.md`; benchmark results JSON |
| F20 | NL2SQL warehouse size | `1,028,160` rows | `NL2SQLAgent/README.md`, Performance table |
| F21 | NL2SQL query latency | measured `78–235 ms`; documented under `250 ms` | `NL2SQLAgent/README.md`, Performance table |
| F22 | NL2SQL end-to-end latency | approximately `25 s → 7 s` | `public/resume/Zhao_Tang_Resume_DataAI_2026-10-21.pdf` |
| F23 | NL2SQL tests | `81` backend + `51` frontend | `public/resume/Zhao_Tang_Resume_DataAI_2026-10-21.pdf` |
| F24 | nanotrack validation run | `10,000` frames; anisotropic diffusion | `nanoparticle-video-pipeline/README.md`; tracking-report preview |

## Claims that must not be published

- Do not publish the phone number.
- Do not publish the legacy Rice email address from older resume versions.
- Do not call Clickstream, GraphAtlas, or NL2SQLAgent production systems.
- Do not imply that synthetic corporate entities or benchmark questions are real customer data.
- Do not say the research publications were produced by the 2026 nanotrack Python implementation.
- Do not state that the portfolio site is “available for opportunities” unless Zhao Tang explicitly adds that status.
- Do not present a generic `100M+` claim beside a personal portfolio project; attribute it to Intuit data products.

## Copy QA checklist

- [x] No placeholder domains or placeholder prose.
- [x] No generic “passionate engineer” language.
- [x] Positioning matches the approved `Data & AI Systems` direction.
- [x] Contact details match approved values.
- [x] Every public metric maps to F01–F24.
- [x] Portfolio/demo boundaries are explicit.
- [x] CTA labels are consistent and short.
