---
title: "nanotrack"
category: "Research data infrastructure"
summary: "A scientific video-tracking pipeline rebuilt from MATLAB into a reproducible Python system with orchestration, observability, and CI."
deck: "A single-molecule video-tracking pipeline rebuilt from MATLAB into a reproducible Python system with serving, orchestration, observability, and CI."
boundary: "Research software. The original methodology supports published work; the open-source Python pipeline is a 2026 engineering reimplementation."
problem: "Scientific video analysis was trapped in a research workflow that was difficult to reproduce, parallelize, monitor, and hand to another engineer."
metrics:
  - value: "15 h → 30 min"
    label: "cluster processing"
  - value: "6"
    label: "peer-reviewed publications"
  - value: "10k"
    label: "validation frames"
stack:
  - "Python"
  - "NumPy"
  - "OpenCV"
  - "scikit-image"
  - "Dask"
  - "Airflow"
  - "FastAPI"
  - "Prometheus / Grafana"
repository: "https://github.com/zt5rice/nanoparticle-video-pipeline"
poster: "/assets/portfolio/projects/nanotrack/tracking-report-10k-preview.webp"
posterWidth: 1240
posterHeight: 1140
order: 4
architecture:
  primary:
    - label: "Video input"
      detail: "synthetic, TIFF, ND2"
    - label: "Preprocess"
      detail: "NumPy / OpenCV / skimage"
    - label: "Detect"
      detail: "threshold + connected components"
    - label: "Track"
      detail: "nearest-neighbor + gap fill"
    - label: "Features"
      detail: "MSD, MSAD, orientation"
    - label: "Validate"
      detail: "quality checks"
    - label: "Export"
      detail: "CSV, JSON, QC, overlay"
  supporting:
    - label: "Airflow"
      detail: "pipeline orchestration"
    - label: "Dask / SLURM"
      detail: "parallel chunk processing"
    - label: "Prometheus / Grafana"
      detail: "runtime and error metrics"
  caption: "Synthetic and real-data support · provenance preserved per run"
built:
  - "Reimplemented detection, tracking, orientation unwrapping, feature extraction, and validation in a Python package."
  - "Added interchangeable NumPy, OpenCV, and scikit-image preprocessing backends."
  - "Parallelized chunked processing with Dask and documented a SLURM path for long cluster runs."
  - "Built a FastAPI service, Airflow DAG, Docker Compose stack, Prometheus metrics, and a provisioned Grafana dashboard."
  - "Added immutable run artifacts, checkpoint resume, self-contained QC reports, tracking overlays, and GitHub Actions CI."
evidence:
  - value: "15 h → 30 min"
    label: "processing time"
    detail: "Cluster parallelization mirrors the original research workflow."
    sourceLabel: "nanotrack README — overview"
    sourceUrl: "https://github.com/zt5rice/nanoparticle-video-pipeline/blob/main/README.md#overview"
  - value: "6"
    label: "peer-reviewed publications"
    detail: "Google Scholar lists six journal articles; additional conference abstracts, posters, and presentations are not counted as publications."
    sourceLabel: "Google Scholar profile"
    sourceUrl: "https://scholar.google.com/citations?user=WlAErpUAAAAJ&hl=en"
  - value: "10,000"
    label: "validation frames"
    detail: "Synthetic single-molecule run with anisotropic diffusion."
    sourceLabel: "nanotrack README — example outputs"
    sourceUrl: "https://github.com/zt5rice/nanoparticle-video-pipeline/blob/main/README.md#example-outputs"
  - value: ">99%"
    label: "data consistency"
    detail: "Automated validation in the research workflow."
    sourceLabel: "Approved resume evidence"
    sourceUrl: "https://github.com/zt5rice/nanoparticle-video-pipeline/blob/main/README.md"
media:
  - type: "image"
    src: "/assets/portfolio/projects/nanotrack/tracking-overlay.webp"
    alt: "Animated nanoparticle tracking overlay showing a detected molecule and trajectory"
    caption: "Tracking overlay generated from a single-molecule video."
    width: 300
    height: 300
  - type: "image"
    src: "/assets/portfolio/projects/nanotrack/tracking-report-10k-preview.webp"
    alt: "Ten-thousand-frame nanotrack QC report with trajectory, MSD, MSAD, and summary panels"
    caption: "A 10,000-frame validation report with parallel/perpendicular MSD behavior."
    width: 1240
    height: 1140
  - type: "image"
    src: "/assets/portfolio/projects/nanotrack/grafana-preview.webp"
    alt: "Grafana dashboard for nanotrack frames processed, errors, and runtime latency"
    caption: "Runtime, throughput, and error observability in Grafana."
    width: 1430
    height: 935
  - type: "image"
    src: "/assets/portfolio/projects/nanotrack/airflow-preview.webp"
    alt: "Airflow DAG for nanotrack preprocessing, detection, tracking, validation, and export"
    caption: "Airflow coordinates the end-to-end analysis and export pipeline."
    width: 1540
    height: 550
limitations:
  - "Synthetic data is the default demo path; real TIFF and ND2 loaders exist but are not part of every CI run."
  - "The Python package is an engineering reimplementation, not a claim that every historical publication was produced with this exact codebase."
sources:
  - label: "Repository"
    url: "https://github.com/zt5rice/nanoparticle-video-pipeline"
  - label: "System design"
    url: "https://github.com/zt5rice/nanoparticle-video-pipeline/blob/main/docs/system-design.md"
  - label: "Example outputs"
    url: "https://github.com/zt5rice/nanoparticle-video-pipeline/blob/main/README.md#example-outputs"
---

The research background shaped how I build software: preserve provenance, make the measurement repeatable, and design for the next person who has to run it.
