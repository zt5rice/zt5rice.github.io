import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

const work = defineCollection({
  loader: glob({
    base: "./src/content/work",
    pattern: "**/*.{md,mdx}",
  }),
  schema: z.object({
    title: z.string(),
    category: z.string(),
    summary: z.string(),
    boundary: z.string(),
    metrics: z.array(z.string()).min(1),
    stack: z.array(z.string()).min(1),
    repository: z.url(),
    demo: z.url().optional(),
    poster: z.string().startsWith("/"),
    video: z.string().startsWith("/").optional(),
    order: z.number().int().nonnegative(),
  }),
});

export const collections = { work };
