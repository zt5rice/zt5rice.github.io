import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const playwrightModule = process.env.PLAYWRIGHT_MODULE || "playwright";
const { chromium } = await import(playwrightModule);

const root = fileURLToPath(new URL(".", import.meta.url));
const baseURL = process.env.BASE_URL || "http://127.0.0.1:4321";
const executablePath =
  process.env.CHROME_PATH ||
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";

const routes = [
  "/",
  "/work/clickstream/",
  "/work/graphatlas/",
  "/work/nl2sqlagent/",
  "/work/nanotrack/",
  "/404.html",
];

const viewports = [
  { width: 1440, height: 900 },
  { width: 768, height: 1024 },
  { width: 390, height: 844 },
];

const failures = [];
const results = {
  baseURL,
  routes: [],
  links: [],
  assets: [],
  console: [],
  accessibility: {},
  screenshots: [],
};

const browser = await chromium.launch({ headless: true, executablePath });

async function loadPage(page, route) {
  const response = await page.goto(`${baseURL}${route}`, {
    waitUntil: "networkidle",
  });
  if (!response || response.status() !== 200) {
    failures.push({
      type: "route-status",
      route,
      status: response?.status() ?? null,
    });
  }

  const height = await page.evaluate(
    () => document.documentElement.scrollHeight,
  );
  for (let y = 0; y < height; y += 600) {
    await page.evaluate((offset) => {
      window.scrollTo({ top: offset, behavior: "instant" });
    }, y);
    await page.waitForTimeout(160);
  }
  await page.evaluate(() => {
    window.scrollTo({ top: document.documentElement.scrollHeight, behavior: "instant" });
  });
  await page.waitForTimeout(400);
  const reduceMotion = await page.evaluate(() =>
    matchMedia("(prefers-reduced-motion: reduce)").matches,
  );
  if (!reduceMotion) {
    await page.waitForFunction(
      () =>
        [...document.querySelectorAll("[data-reveal]")].every((element) =>
          element.classList.contains("is-visible"),
        ),
      { timeout: 3500 },
    );
  }
  await page.evaluate(() => window.scrollTo({ top: 0, behavior: "instant" }));
  await page.waitForTimeout(100);
}

for (const viewport of viewports) {
  const context = await browser.newContext({
    viewport,
    reducedMotion: "no-preference",
  });
  const page = await context.newPage();
  const consoleErrors = [];

  page.on("console", (message) => {
    if (message.type() === "error") consoleErrors.push(message.text());
  });
  page.on("pageerror", (error) => {
    consoleErrors.push(error.message);
  });

  for (const route of routes) {
    await loadPage(page, route);

    const metrics = await page.evaluate(() => {
      const heroTitle = document.querySelector("#hero-title");
      let heroNameLines = null;

      if (heroTitle) {
        const nameRange = document.createRange();
        nameRange.selectNodeContents(heroTitle);
        heroNameLines = nameRange.getClientRects().length;
      }

      return {
        title: document.title,
        h1Count: document.querySelectorAll("h1").length,
        canonical:
          document.querySelector('link[rel="canonical"]')?.getAttribute("href") ??
          null,
        scrollWidth: document.documentElement.scrollWidth,
        innerWidth: window.innerWidth,
        heroNameLines,
        avifImages: [...document.querySelectorAll("picture img")].filter((img) =>
          img.currentSrc.endsWith(".avif"),
        ).length,
        images: document.querySelectorAll("img").length,
        videos: [...document.querySelectorAll("video")].map((video) => ({
          autoplay: video.autoplay,
          controls: video.controls,
          preload: video.preload,
          poster: Boolean(video.poster),
        })),
        robots:
          document.querySelector('meta[name="robots"]')?.getAttribute("content") ??
          null,
      };
    });

    if (metrics.h1Count !== 1) {
      failures.push({ type: "h1-count", viewport, route, ...metrics });
    }
    if (!metrics.title || !metrics.canonical) {
      failures.push({ type: "seo-meta", viewport, route, ...metrics });
    }
    if (metrics.scrollWidth > metrics.innerWidth) {
      failures.push({ type: "horizontal-overflow", viewport, route, ...metrics });
    }
    if (route === "/" && viewport.width >= 390 && metrics.heroNameLines !== 1) {
      failures.push({ type: "hero-name-wrap", viewport, ...metrics });
    }
    if (route === "/404.html" && !metrics.robots?.includes("noindex")) {
      failures.push({ type: "404-noindex", viewport, route, robots: metrics.robots });
    }

    results.routes.push({ viewport, route, ...metrics });
  }

  if (consoleErrors.length > 0) {
    failures.push({ type: "console-errors", viewport, consoleErrors });
    results.console.push({ viewport, errors: consoleErrors });
  }

  await context.close();
}

for (const viewport of viewports) {
  const screenshotContext = await browser.newContext({
    viewport,
    reducedMotion: "reduce",
  });
  const screenshotPage = await screenshotContext.newPage();
  await loadPage(screenshotPage, "/");
  const screenshot = path.join(root, "screenshots", `home-${viewport.width}.png`);
  await mkdir(path.dirname(screenshot), { recursive: true });
  await screenshotPage.screenshot({ path: screenshot, fullPage: true });
  results.screenshots.push(path.relative(root, screenshot));
  await screenshotContext.close();
}

const linkContext = await browser.newContext({ viewport: viewports[0] });
const linkPage = await linkContext.newPage();
const checked = new Set();
const checkedAssets = new Set();
for (const route of routes) {
  await loadPage(linkPage, route);
  const hrefs = await linkPage.locator('a[href^="/"]').evaluateAll((links) =>
    links.map((link) => link.getAttribute("href")).filter(Boolean),
  );
  for (const href of hrefs) {
    const target = new URL(href, baseURL);
    target.hash = "";
    if (checked.has(target.href)) continue;
    checked.add(target.href);
    const response = await linkContext.request.get(target.href);
    results.links.push({
      source: route,
      href,
      status: response.status(),
      contentType: response.headers()["content-type"] ?? null,
    });
    if (!response.ok()) {
      failures.push({
        type: "internal-link",
        source: route,
        href,
        status: response.status(),
      });
    }
  }

  const assets = await linkPage.evaluate(() => {
    const urls = [];
    document.querySelectorAll("img").forEach((image) => {
      if (image.currentSrc) urls.push(image.currentSrc);
    });
    document.querySelectorAll("video").forEach((video) => {
      if (video.poster) urls.push(video.poster);
      if (video.currentSrc) urls.push(video.currentSrc);
      video.querySelectorAll("source").forEach((source) => {
        if (source.src) urls.push(source.src);
      });
    });
    return [...new Set(urls)];
  });
  for (const asset of assets) {
    const target = new URL(asset, baseURL);
    if (checkedAssets.has(target.href)) continue;
    checkedAssets.add(target.href);
    const response = await linkContext.request.get(target.href);
    results.assets.push({
      source: route,
      href: target.pathname,
      status: response.status(),
      contentType: response.headers()["content-type"] ?? null,
    });
    if (!response.ok()) {
      failures.push({
        type: "asset",
        source: route,
        href: target.pathname,
        status: response.status(),
      });
    }
  }
}

await linkPage.goto(`${baseURL}/work/graphatlas/`, {
  waitUntil: "networkidle",
});
const videos = await linkPage.locator("video").evaluateAll((items) =>
  items.map((video) => ({
    autoplay: video.autoplay,
    controls: video.controls,
    preload: video.preload,
    poster: Boolean(video.poster),
  })),
);
if (
  videos.length !== 3 ||
  videos.some((video) => video.autoplay || !video.controls || video.preload !== "none" || !video.poster)
) {
  failures.push({ type: "video-policy", videos });
}
results.accessibility.videos = videos;
await linkContext.close();

const keyboardContext = await browser.newContext({ viewport: viewports[0] });
const keyboardPage = await keyboardContext.newPage();
await keyboardPage.goto(baseURL, { waitUntil: "networkidle" });
const focusOrder = [];
for (let index = 0; index < 7; index += 1) {
  await keyboardPage.keyboard.press("Tab");
  focusOrder.push(
    await keyboardPage.evaluate(() => {
      const active = document.activeElement;
      const style = getComputedStyle(active);
      return {
        tag: active?.tagName ?? null,
        text: active?.textContent?.trim().slice(0, 40) ?? "",
        href: active?.getAttribute?.("href") ?? null,
        outlineWidth: style.outlineWidth,
        outlineStyle: style.outlineStyle,
      };
    }),
  );
}
results.accessibility.focusOrder = focusOrder;
if (
  focusOrder[0]?.href !== "#main" ||
  focusOrder.some((item) => item.outlineStyle !== "solid" || item.outlineWidth !== "2px")
) {
  failures.push({ type: "keyboard-focus", focusOrder });
}
await keyboardContext.close();

const mobileContext = await browser.newContext({
  viewport: { width: 390, height: 844 },
});
const mobilePage = await mobileContext.newPage();
await mobilePage.goto(baseURL, { waitUntil: "networkidle" });
await mobilePage.locator("[data-mobile-nav] summary").click();
const menuOpen = await mobilePage.locator("[data-mobile-nav]").evaluate((el) => el.open);
await mobilePage.keyboard.press("Escape");
const menuClosed = await mobilePage.locator("[data-mobile-nav]").evaluate((el) => !el.open);
results.accessibility.mobileMenu = { menuOpen, menuClosed };
if (!menuOpen || !menuClosed) failures.push({ type: "mobile-menu", menuOpen, menuClosed });
await mobileContext.close();

const reducedContext = await browser.newContext({
  viewport: { width: 390, height: 844 },
  reducedMotion: "reduce",
});
const reducedPage = await reducedContext.newPage();
await reducedPage.goto(baseURL, { waitUntil: "networkidle" });
const reduced = await reducedPage.evaluate(() => ({
  mediaMatches: matchMedia("(prefers-reduced-motion: reduce)").matches,
  heroAnimation: getComputedStyle(document.querySelector(".hero-copy > *"))
    .animationName,
  revealOpacity: getComputedStyle(document.querySelector("[data-reveal]")).opacity,
  revealTransform: getComputedStyle(document.querySelector("[data-reveal]"))
    .transform,
}));
results.accessibility.reducedMotion = reduced;
if (
  !reduced.mediaMatches ||
  reduced.revealOpacity !== "1" ||
  reduced.revealTransform !== "none"
) {
  failures.push({ type: "reduced-motion", reduced });
}
await reducedContext.close();

await browser.close();
results.failures = failures;
results.passed = failures.length === 0;

await mkdir(path.join(root, "screenshots"), { recursive: true });
await writeFile(
  path.join(root, "results.json"),
  `${JSON.stringify(results, null, 2)}\n`,
);

console.log(JSON.stringify({ passed: results.passed, failures, links: results.links.length }, null, 2));
process.exitCode = failures.length === 0 ? 0 : 1;
