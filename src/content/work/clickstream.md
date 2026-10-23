---
title: Clickstream
category: Streaming data platform
summary: An end-to-end streaming platform that turns high-volume events into monitored, queryable data products.
boundary: Portfolio system using synthetic traffic and short-run local or kind-cluster measurements.
metrics:
  - "~100 events/s"
  - "p95 181 ms"
  - "111 tests"
stack:
  - Python
  - Kafka
  - Spark
  - PostgreSQL
  - ClickHouse
  - FastAPI
repository: https://github.com/zt5rice/clickstream
poster: /assets/portfolio/projects/clickstream/grafana-dashboard.webp
order: 1
---

Clickstream demonstrates the full path from event generation to a monitored read
API: ingestion, streaming windows, dead-letter handling, curated storage,
read-only serving, data quality, and production-style failure drills.
