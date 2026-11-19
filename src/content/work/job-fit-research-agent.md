---
title: "Job Fit Research Agent"
category: "Controlled AI research agent"
summary: "An evidence-backed job-fit prototype that separates LLM extraction from deterministic scoring and routes uncertain cases to human review."
deck: "A controlled DeepAgents workflow that turns local job descriptions into inspectable recommendations with exact source quotes, a fixed rubric, and an audit manifest."
boundary: "Independent offline-first prototype using synthetic profiles and job descriptions. Not production software, not a hiring system, and not used to submit applications."
problem: "Job descriptions mix requirements, preferences, and legal constraints, while a single LLM-generated score can hide missing evidence, prompt injection, or work-authorization blockers. The system needed to separate extraction from judgment and make every recommendation inspectable."
metrics:
  - value: "15 / 15"
    label: "synthetic evaluation agreement"
  - value: "100%"
    label: "evidence coverage"
  - value: "40"
    label: "unit tests"
stack:
  - "Python"
  - "DeepAgents"
  - "LangChain"
  - "OpenAI-compatible LLMs"
  - "unittest"
  - "GitHub Actions"
repository: "https://github.com/zt5rice/job-fit-research-agent"
poster: "/assets/portfolio/projects/job-fit/overview.webp"
posterWidth: 1600
posterHeight: 900
order: 5
architecture:
  primary:
    - label: "Profile + jobs"
      detail: "local, untrusted input"
    - label: "DeepAgents planner"
      detail: "plans + delegates"
    - label: "job_analyst"
      detail: "typed extraction"
    - label: "Evidence validator"
      detail: "quotes + line spans"
    - label: "Deterministic rubric"
      detail: "30/30/15/15/10"
    - label: "Review gate"
      detail: "uncertain or high impact"
    - label: "Reports"
      detail: "JSON + Markdown + manifest"
  supporting:
    - label: "Filesystem backend"
      detail: "isolated local context"
    - label: "Input hashing"
      detail: "SHA-256 audit trail"
    - label: "Eval corpus"
      detail: "15 synthetic cases"
    - label: "CI gate"
      detail: "40 tests + regressions"
  caption: "Offline demo path · model extraction separated from deterministic scoring"
built:
  - "Built a real DeepAgents planner with a narrow job_analyst subagent, typed local tools, and a filesystem-backed execution context."
  - "Kept scoring outside the model: deterministic Python validates the structured facts and computes the only score that reaches the report."
  - "Added evidence validation for exact quotes, line locators, duplicate IDs, malformed output, prompt injection, and hard authorization blockers."
  - "Built a human-review gate plus controlled deterministic fallback when live model output cannot be validated."
  - "Added run manifests with input hashes, tool events, rubric versions, warnings, and limitations, backed by 40 unit tests and a 15-case regression corpus."
evidence:
  - value: "15 / 15"
    label: "synthetic recommendation agreement"
    detail: "Six apply, three investigate, and six skip labels matched the deterministic pipeline in the current offline evaluation."
    sourceLabel: "Labeled evaluation corpus"
    sourceUrl: "https://github.com/zt5rice/job-fit-research-agent/blob/main/evals/labeled_jobs.json"
  - value: "100%"
    label: "mean evidence coverage"
    detail: "Extracted requirements are checked against exact source quotes and one-based line locators."
    sourceLabel: "Evaluation metrics and validation code"
    sourceUrl: "https://github.com/zt5rice/job-fit-research-agent/blob/main/src/job_fit/evaluation.py"
  - value: "0"
    label: "hard-blocker false applies"
    detail: "Sponsorship, citizenship, and clearance conflicts cap the score and route the result to review."
    sourceLabel: "Regression gate"
    sourceUrl: "https://github.com/zt5rice/job-fit-research-agent/blob/main/src/job_fit/scoring.py"
  - value: "40"
    label: "unit tests"
    detail: "Coverage includes deterministic scoring, evidence tampering, prompt injection, privacy, reporting, and the real DeepAgents assembly."
    sourceLabel: "GitHub Actions CI"
    sourceUrl: "https://github.com/zt5rice/job-fit-research-agent/blob/main/.github/workflows/ci.yml"
media:
  - type: "image"
    src: "/assets/portfolio/projects/job-fit/overview.webp"
    alt: "Job Fit Research Agent overview showing apply, investigate, and skip recommendations plus the controlled agent architecture"
    caption: "Sanitized offline evaluation output with the planner-to-deterministic-scoring control plane."
    width: 1600
    height: 900
  - type: "image"
    src: "/assets/portfolio/projects/job-fit/audit.webp"
    alt: "Job Fit Research Agent assessment showing score breakdown, line-cited evidence, and run manifest"
    caption: "The score breakdown, source evidence, review state, and audit-manifest fields remain inspectable."
    width: 1600
    height: 900
limitations:
  - "The 100% evaluation result is measured on a 15-case synthetic corpus with deterministic offline extraction; it does not establish production hiring accuracy."
  - "Live extraction quality depends on the configured model provider, and the rubric is not calibrated against a large hiring dataset."
  - "The prototype does not scrape authenticated job boards, submit applications, contact employers, or make hiring decisions."
sources:
  - label: "Repository"
    url: "https://github.com/zt5rice/job-fit-research-agent"
  - label: "Architecture and boundaries"
    url: "https://github.com/zt5rice/job-fit-research-agent/blob/main/README.md"
  - label: "Five-minute demo"
    url: "https://github.com/zt5rice/job-fit-research-agent/blob/main/docs/DEMO.md"
  - label: "Sanitized ranked report"
    url: "https://github.com/zt5rice/job-fit-research-agent/blob/main/examples/sample_outputs/ranked_jobs.md"
---

The important design decision is not using an LLM to make the final decision. The model extracts structure, while deterministic code verifies evidence, applies the rubric, and forces uncertain or high-impact cases into human review.
