---
title: "Clickstream"
category: "Streaming data platform"
summary: "An end-to-end streaming platform that turns high-volume events into monitored, queryable data products."
deck: "A production-shaped clickstream pipeline built to test the full path from event generation to a monitored read API."
boundary: "Portfolio build using synthetic events and short-run local or kind-cluster measurements. Not an employer production system."
problem: "Streaming projects often stop at a dashboard. The harder question is whether the event contract, state model, query layer, and failure paths hold together when data is late, duplicated, malformed, or temporarily unavailable."
metrics:
  - value: "~100 events/s"
    label: "producer throughput"
  - value: "p95 181 ms"
    label: "API under load"
  - value: "111"
    label: "Python tests"
stack:
  - "Python"
  - "Kafka"
  - "Spark"
  - "PostgreSQL"
  - "ClickHouse"
  - "FastAPI"
repository: "https://github.com/zt5rice/clickstream"
poster: "/assets/portfolio/projects/clickstream/grafana-dashboard.webp"
posterWidth: 1600
posterHeight: 1610
order: 1
architecture:
  primary:
    - label: "Producer"
      detail: "~100 events/s"
    - label: "Kafka"
      detail: "clicks.raw + DLQ"
    - label: "Spark"
      detail: "1-minute windows"
    - label: "PostgreSQL"
      detail: "curated aggregates"
    - label: "ClickHouse"
      detail: "analytics storage"
    - label: "FastAPI"
      detail: "read-only API"
    - label: "Grafana"
      detail: "SLIs and alerts"
  supporting:
    - label: "Airflow"
      detail: "freshness and rollups"
    - label: "dbt"
      detail: "models and tests"
    - label: "Soda"
      detail: "data-quality checks"
    - label: "Terraform / EKS"
      detail: "time-boxed cloud run"
  caption: "Synthetic traffic · local and kind-cluster measurements"
built:
  - "Built a deterministic producer and Kafka ingestion path, then processed one-minute windows in Spark Structured Streaming with watermarking and a dead-letter topic."
  - "Modeled curated data for PostgreSQL and analytical data for ClickHouse, with idempotent upserts and a read-only FastAPI serving layer."
  - "Added Airflow orchestration, dbt models and tests, data-quality checks, Redis caching, rate limiting, and a Go operations CLI."
  - "Instrumented the system with Prometheus and Grafana, then added SLOs, runbooks, k6 load tests, and chaos drills."
  - "Deployed through Docker Compose and kind/Helm, with a time-boxed Terraform/EKS run that was destroyed in the same session."
evidence:
  - value: "~100 events/s"
    label: "steady-state producer"
    detail: "Zero failed events in the recorded run."
    sourceLabel: "Clickstream README — measured metrics"
    sourceUrl: "https://github.com/zt5rice/clickstream/blob/main/README.md#measured-metrics-by-phase"
  - value: "p95 180.6 ms"
    label: "API latency"
    detail: "46 requests/s with 0% errors in the k6 load test."
    sourceLabel: "Clickstream README — Phase 4"
    sourceUrl: "https://github.com/zt5rice/clickstream/blob/main/README.md#phase-4--reliability-2026-09-0708"
  - value: "111"
    label: "Python tests"
    detail: "Also 15/15 dbt tests and 11/11 data-quality checks passed."
    sourceLabel: "Clickstream README — verification"
    sourceUrl: "https://github.com/zt5rice/clickstream/blob/main/README.md#phase-2--engineering-verification-2026-09-04"
  - value: "21 s / 33 s"
    label: "chaos recovery"
    detail: "API and Kafka pod recovery time under kind."
    sourceLabel: "Clickstream README — Phase 4"
    sourceUrl: "https://github.com/zt5rice/clickstream/blob/main/README.md#phase-4--reliability-2026-09-0708"
media:
  - type: "image"
    src: "/assets/portfolio/projects/clickstream/grafana-dashboard.webp"
    alt: "Clickstream Grafana dashboard showing freshness, Kafka throughput, queue depth, and API latency panels"
    caption: "Operational dashboard for pipeline freshness, throughput, and API latency."
    width: 1600
    height: 1610
  - type: "image"
    src: "/assets/portfolio/projects/clickstream/prometheus-alerts.webp"
    alt: "Prometheus alert rules for Kafka consumer lag, API latency, and dead-letter queue depth"
    caption: "Alert rules cover lag, API latency, and dead-letter messages."
    width: 1600
    height: 1610
  - type: "image"
    src: "/assets/portfolio/projects/clickstream/api-docs.webp"
    alt: "OpenAPI documentation for the read-only Clickstream API"
    caption: "The read-only API exposes summary, events, timeline, and health endpoints."
    width: 1600
    height: 1610
limitations:
  - "The system uses synthetic events, a short measurement window, and a single-node Kafka configuration."
  - "It demonstrates production-shaped engineering, not production traffic, multi-region resilience, or a long-running SLO history."
sources:
  - label: "Repository"
    url: "https://github.com/zt5rice/clickstream"
  - label: "Architecture and measured results"
    url: "https://github.com/zt5rice/clickstream/blob/main/README.md"
  - label: "Design trade-offs"
    url: "https://github.com/zt5rice/clickstream/blob/main/docs/design-decisions.md"
---

Clickstream treats observability, data quality, failure recovery, and cost control as part of the pipeline rather than follow-up work.
