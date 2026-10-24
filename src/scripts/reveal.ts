const elements = Array.from(
  document.querySelectorAll<HTMLElement>("[data-reveal]"),
);
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

if (elements.length > 0 && "IntersectionObserver" in window && !reduceMotion.matches) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    {
      threshold: 0.08,
      rootMargin: "0px 0px -32px 0px",
    },
  );

  elements.forEach((element) => {
    const bounds = element.getBoundingClientRect();
    if (bounds.top < window.innerHeight && bounds.bottom > 0) {
      element.classList.add("is-visible");
      return;
    }
    observer.observe(element);
  });

  document.documentElement.classList.add("reveal-ready");

  // Fail open if the observer never settles on a slow or embedded browser.
  window.setTimeout(() => {
    elements.forEach((element) => element.classList.add("is-visible"));
  }, 2500);
}
