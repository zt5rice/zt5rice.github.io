export const site = {
  url: "https://zt5rice.github.io",
  title: "Dr. Zhao Tang — Software Engineer, Data & AI Systems",
  description:
    "Dr. Zhao Tang builds reliable data platforms, measurable AI products, and production systems. Explore selected work across streaming data, GraphRAG, natural-language analytics, and scientific computing.",
  ogImage: "/og/og-portfolio.png",
  ogImageWidth: 1200,
  ogImageHeight: 630,
  person: {
    name: "Dr. Zhao Tang",
    givenName: "Zhao",
    familyName: "Tang",
    jobTitle: "Software Engineer",
    location: "San Diego, California",
    email: "ztangintuit@gmail.com",
    linkedin: "https://www.linkedin.com/in/tzhao7-sde/",
    github: "https://github.com/zt5rice",
    scholar:
      "https://scholar.google.com/citations?user=WlAErpUAAAAJ&hl=en",
  },
  resume: "/resume/Zhao_Tang_Resume_DataAI_2026-10-21.pdf",
} as const;

export const navigation = [
  { label: "Work", href: "/#work" },
  { label: "Experience", href: "/#experience" },
  { label: "About", href: "/#about" },
  { label: "Research", href: "/#research" },
  { label: "Contact", href: "/#contact" },
] as const;

export const personSchema = {
  "@context": "https://schema.org",
  "@type": "Person",
  name: site.person.name,
  givenName: site.person.givenName,
  familyName: site.person.familyName,
  jobTitle: site.person.jobTitle,
  description: site.description,
  url: site.url,
  image: new URL(site.ogImage, site.url).toString(),
  email: `mailto:${site.person.email}`,
  address: {
    "@type": "PostalAddress",
    addressLocality: "San Diego",
    addressRegion: "CA",
    addressCountry: "US",
  },
  sameAs: [site.person.github, site.person.linkedin, site.person.scholar],
};
