export const experience = [
  {
    role: "Software Engineer",
    team: "Customer Product & Experience Optimization",
    company: "Intuit",
    context: "Customer Product Organization · TurboTax",
    dates: "07/2025 — 07/2026",
    summary:
      "Owned production data quality and measurement while serving as primary on-call engineer.",
    bullets: [
      "Cut MTTR by 40% using distributed tracing and root-cause analysis, with durable corrective actions and runbooks.",
      "Led a cross-organization remediation of millions of missing records and aligned three organizations on one metric definition and validation standard.",
      "Raised experiment device coverage by 10+ percentage points, moving from the mid-60s to the high-70s.",
      "Upgraded batch pipelines to incremental processing, reducing peak processing time from 7 hours to 15 minutes and peak infrastructure cost by 95%.",
      "Built validation and monitoring that surfaced incorrect data before it reached reporting.",
    ],
  },
  {
    role: "Software Engineer",
    team: "Data Platform & Analytics Infrastructure",
    company: "Intuit",
    context: "Analytics, AI & Data · TurboTax and QuickBooks",
    dates: "03/2024 — 07/2025",
    summary:
      "Built real-time data platforms and foundational datasets for products used by more than 100 million people.",
    bullets: [
      "Built real-time pipelines and datasets powering daily decisions for 100M+ TurboTax and QuickBooks users.",
      "Mapped dependencies across 100+ pipelines and approximately 1,000 tables, cutting manual cross-team approval coordination by about 50%.",
      "Fixed a multi-year stateful defect, restoring cumulative tracking since 2020 for 10M+ unique visitors and 1M+ daily sessions.",
      "Used internal AI tooling to deliver 10+ pipelines with code review and end-to-end validation.",
    ],
  },
  {
    role: "Research Specialist",
    team: "Research Data Infrastructure",
    company: "Rice University",
    context: "George R. Brown School of Engineering and Computing",
    dates: "06/2023 — 03/2024",
    summary:
      "Engineered reproducible data infrastructure for multi-terabyte scientific datasets.",
    bullets: [
      "Built Python workflows with automated validation and greater than 99% data consistency for scientific users.",
      "Parallelized multi-terabyte video and unstructured-data processing on HPC clusters.",
      "Re-engineered a MATLAB tracking methodology into the open-source nanotrack Python pipeline.",
    ],
  },
  {
    role: "Visiting Scholar",
    team: "Computational Imaging & Machine Learning",
    company: "Rice University",
    context: "Chemical and Biomolecular Engineering",
    dates: "05/2022 — 05/2023",
    summary:
      "Built computational-imaging and machine-learning pipelines for single-molecule and nanoparticle analysis.",
    bullets: [
      "Developed automated image-processing and optical-analysis software in Python and MATLAB.",
      "Reduced per-experiment processing time from 15 hours to 30 minutes through cluster parallelization.",
      "Published methods and datasets that support 6 peer-reviewed papers, with additional conference posters and presentations.",
    ],
  },
] as const;

export const focusAreas = [
  "Reliable data platforms",
  "Retrieval and evaluation for AI systems",
  "Production observability",
  "Scientific computing",
] as const;

export const education = [
  "PhD, Chemical & Biomolecular Engineering — Rice University",
  "MS, Computer Science — Georgia Institute of Technology (in progress)",
  "DBA, Business Analytics — Westcliff University (in progress)",
  "BS, Chemical Engineering — Purdue University",
] as const;

export const skillGroups = [
  {
    label: "Data & streaming",
    items: [
      "Python",
      "SQL",
      "Spark",
      "Kafka",
      "Airflow",
      "dbt",
      "Databricks",
      "Delta Lake",
      "PostgreSQL",
      "ClickHouse",
      "Redis",
    ],
  },
  {
    label: "Cloud & reliability",
    items: [
      "AWS",
      "Docker",
      "Kubernetes",
      "Helm",
      "Terraform",
      "GitHub Actions",
      "Prometheus",
      "Grafana",
      "Linux",
    ],
  },
  {
    label: "Backend & APIs",
    items: ["FastAPI", "REST", "Server-Sent Events", "TypeScript", "Hono"],
  },
  {
    label: "AI & retrieval",
    items: [
      "pgvector",
      "RAG / GraphRAG",
      "Reciprocal Rank Fusion",
      "LLM evaluation",
      "LangChain",
    ],
  },
  {
    label: "Languages",
    items: ["Python", "SQL", "Scala", "Go", "TypeScript / JavaScript", "Bash"],
  },
] as const;

export const researchAreas = [
  "Computational imaging",
  "Single-molecule tracking",
  "Machine learning",
  "Research data infrastructure",
] as const;
