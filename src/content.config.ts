import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

const metric = z.object({
  value: z.string(),
  label: z.string(),
});

const architectureNode = z.object({
  label: z.string(),
  detail: z.string(),
});

const evidence = z.object({
  value: z.string(),
  label: z.string(),
  detail: z.string(),
  sourceLabel: z.string(),
  sourceUrl: z.url(),
});

const media = z.object({
  type: z.enum(["image", "video"]),
  src: z.string().startsWith("/"),
  poster: z.string().startsWith("/").optional(),
  alt: z.string(),
  caption: z.string(),
  width: z.number().int().positive(),
  height: z.number().int().positive(),
});

const work = defineCollection({
  loader: glob({
    base: "./src/content/work",
    pattern: "**/*.{md,mdx}",
  }),
  schema: z.object({
    title: z.string(),
    category: z.string(),
    summary: z.string(),
    deck: z.string(),
    boundary: z.string(),
    problem: z.string(),
    metrics: z.array(metric).length(3),
    stack: z.array(z.string()).min(1),
    repository: z.url(),
    demo: z.url().optional(),
    poster: z.string().startsWith("/"),
    posterWidth: z.number().int().positive(),
    posterHeight: z.number().int().positive(),
    order: z.number().int().nonnegative(),
    architecture: z.object({
      primary: z.array(architectureNode).min(1),
      supporting: z.array(architectureNode).default([]),
      caption: z.string(),
    }),
    built: z.array(z.string()).min(1),
    evidence: z.array(evidence).min(1),
    media: z.array(media).min(1),
    limitations: z.array(z.string()).min(1),
    sources: z.array(
      z.object({
        label: z.string(),
        url: z.url(),
      }),
    ).min(1),
  }),
});

export const collections = { work };
