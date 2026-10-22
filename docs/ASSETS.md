# Portfolio Asset Manifest

Last reviewed: 2026-10-21

## Purpose

This document records the provenance, intended use, and privacy review for every
portfolio asset selected for the public site. The original source files remain
outside the website repository under:

`/Users/zhaotang/projects/person_website/source-assets/`

Only optimized, public-safe derivatives are committed under:

`public/assets/portfolio/`

## Avatar

| Public file | Source | Treatment |
| --- | --- | --- |
| `avatar/zhao-tang-portrait.webp` | `zt5rice.github.io@97fdef9:images/1614100527021.jpg` | 4:5 crop, EXIF removed, WebP quality 92 |

Source URL:
[professional portrait](https://github.com/zt5rice/zt5rice.github.io/blob/97fdef9fbadd811947e92b586ca7427226537457/images/1614100527021.jpg)

Notes:

- No facial alteration or synthetic upscaling was applied.
- The source is 400 x 400; the public derivative is 400 x 500.
- Heavy full-screen use should be avoided. Use the portrait in the editorial hero
  or About treatment where the available resolution is appropriate.

## Clickstream

| Public file | Local source | Use |
| --- | --- | --- |
| `projects/clickstream/grafana-dashboard.webp` | `clickstream/docs/images/grafana-dashboard.png` | Primary monitoring visual |
| `projects/clickstream/prometheus-alerts.webp` | `clickstream/docs/images/prometheus-alerts.png` | Reliability evidence |
| `projects/clickstream/api-docs.webp` | `clickstream/docs/images/api-docs.png` | API surface evidence |

Repository:
[zt5rice/clickstream](https://github.com/zt5rice/clickstream)

Treatments:

- Resized to 1600 px wide.
- EXIF removed.
- WebP quality 82.
- Browser chrome retained for product context.

Portfolio boundary: this project is a local/portfolio demonstration, not
employer production traffic. Do not describe it as a production system.

## GraphAtlas

| Public file | Local source | Use |
| --- | --- | --- |
| `projects/graphatlas/graphatlas-demo01-poster.webp` | `knowledgeRAG/docs/demos/graphatlas-demo01.mov` | Ingest workflow poster |
| `projects/graphatlas/graphatlas-demo02-poster.webp` | `knowledgeRAG/docs/demos/graphatlas-demo02.mov` | Graph explorer poster |
| `projects/graphatlas/graphatlas-demo03-poster.webp` | `knowledgeRAG/docs/demos/graphatlas-demo03.mov` | QA with evidence poster |
| `projects/graphatlas/media/graphatlas-demo01.mp4` | same | Ingest demo |
| `projects/graphatlas/media/graphatlas-demo02.mp4` | same | Graph explorer demo |
| `projects/graphatlas/media/graphatlas-demo03.mp4` | same | QA and evidence demo |

Repository:
[zt5rice/graphatlas](https://github.com/zt5rice/graphatlas)

Video treatment:

- Converted from QuickTime `.mov` to H.264 MP4 with macOS AVFoundation.
- AVFoundation's default metadata filter was left enabled.
- Playback metadata: 1154 x 950 / 952, durations approximately 19.9 s,
  26.2 s, and 33.4 s.
- Source `.mov` files are not committed to the website repository.

Excluded:

- `graphatlas-demo04.mov` is excluded because the reviewed frame contains only an
  empty terminal and an opaque container hostname. It adds no portfolio value.

Portfolio boundary: GraphAtlas uses a synthetic corpus and a self-built
50-question benchmark. All displayed metrics must retain that context.

## NL2SQLAgent

| Public file | Local source | Use |
| --- | --- | --- |
| `projects/nl2sql/overview.webp` | `NL2SQLAgent/demo.png` | Primary product screenshot |

Repository:
[zt5rice/NL2SQLAgent](https://github.com/zt5rice/NL2SQLAgent)

Treatments:

- EXIF removed.
- WebP quality 86.
- No UI content was altered.

Notes:

- The screenshot shows a local development URL and synthetic sales data.
- No API key, credential, private dataset, or personal contact information is
  visible.

## nanotrack / nanoparticle-video-pipeline

| Public file | Local source | Use |
| --- | --- | --- |
| `projects/nanotrack/tracking-overlay.webp` | `docs/assets/tracking_overlay.gif` | Motion evidence |
| `projects/nanotrack/tracking-qc-preview.webp` | `docs/assets/tracking_qc_preview.png` | Tracking report |
| `projects/nanotrack/tracking-report-10k-preview.webp` | `docs/assets/tracking_report_10k_preview.png` | Long-run evidence |
| `projects/nanotrack/grafana-preview.webp` | `docs/assets/grafana_preview.png` | Pipeline observability |
| `projects/nanotrack/airflow-preview.webp` | `docs/assets/airflow_preview.png` | Orchestration |
| `projects/nanotrack/prometheus-preview.webp` | `docs/assets/prometheus_preview.png` | Monitoring |

Repository:
[zt5rice/nanoparticle-video-pipeline](https://github.com/zt5rice/nanoparticle-video-pipeline)

Treatments:

- Static PNGs converted to WebP with EXIF removed.
- The 30-frame GIF was converted to an animated WebP with the original frame
  duration and continuous looping.
- Synthetic sample data is labeled as such in the source repository.

## Privacy review

Completed checks:

- Manual review of every selected still and video poster.
- WebP metadata inspection: no EXIF, GPS, author, or camera metadata retained.
- String scan across all public derivatives for the old email, approved email,
  phone number, API keys, secrets, passwords, and bearer tokens: no matches.
- Local development URLs are acceptable and appear only as product context.
- No employer data, customer data, credentials, `.env` values, private IPs, or
  private identifiers are visible.

## Usage rules

- Use descriptive alt text based on the visible content, not filenames.
- Lazy-load below-the-fold images and video.
- Provide the poster image before loading GraphAtlas video.
- Keep screenshots inside a framed media surface so the browser chrome does not
  become the dominant visual.
- Do not claim that a portfolio/demo project is production traffic.
