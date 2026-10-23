#!/usr/bin/env python3
"""Generate high-fidelity portfolio mockups from approved local assets."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "design" / "mockups"
SCALE = 2

AVENIR = "/System/Library/Fonts/Avenir Next.ttc"
MENLO = "/System/Library/Fonts/Menlo.ttc"

BG = (9, 11, 13)
PANEL = (18, 21, 24)
PANEL_ALT = (23, 27, 30)
TEXT = (242, 238, 230)
MUTED = (158, 163, 166)
DIM = (111, 118, 122)
ORANGE = (255, 106, 61)
GREEN = (120, 240, 166)
BORDER = (43, 47, 50)
WHITE = (255, 255, 255)

AVATAR = ROOT / "public/assets/portfolio/avatar/zhao-tang-portrait.webp"
CLICKSTREAM = (
    ROOT
    / "public/assets/portfolio/projects/clickstream/grafana-dashboard.webp"
)
GRAPHATLAS = (
    ROOT
    / "public/assets/portfolio/projects/graphatlas/"
    "graphatlas-demo02-poster.webp"
)
NL2SQL = ROOT / "public/assets/portfolio/projects/nl2sql/overview.webp"
NANOTRACK = (
    ROOT
    / "public/assets/portfolio/projects/nanotrack/"
    "tracking-report-10k-preview.webp"
)


class Canvas:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.img = Image.new("RGBA", (width * SCALE, height * SCALE), BG)
        self.draw = ImageDraw.Draw(self.img, "RGBA")
        self._fonts = {}

    def font(self, size: float, style: str = "regular"):
        key = (size, style)
        if key not in self._fonts:
            if style == "mono":
                path, index = MENLO, 0
            elif style == "mono-bold":
                path, index = MENLO, 1
            elif style == "heavy":
                path, index = AVENIR, 8
            elif style == "demi":
                path, index = AVENIR, 2
            elif style == "medium":
                path, index = AVENIR, 5
            elif style == "bold":
                path, index = AVENIR, 0
            else:
                path, index = AVENIR, 7
            self._fonts[key] = ImageFont.truetype(
                path,
                int(size * SCALE),
                index=index,
            )
        return self._fonts[key]

    def rect(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        radius: float = 0,
        fill=None,
        outline=None,
        width: float = 1,
    ):
        self.draw.rounded_rectangle(
            (
                int(x * SCALE),
                int(y * SCALE),
                int((x + w) * SCALE),
                int((y + h) * SCALE),
            ),
            radius=int(radius * SCALE),
            fill=fill,
            outline=outline,
            width=max(1, int(width * SCALE)),
        )

    def line(
        self,
        points,
        fill,
        width: float = 1,
    ):
        self.draw.line(
            [(int(x * SCALE), int(y * SCALE)) for x, y in points],
            fill=fill,
            width=max(1, int(width * SCALE)),
            joint="curve",
        )

    def text(
        self,
        x: float,
        y: float,
        value: str,
        size: float,
        style: str = "regular",
        fill=TEXT,
        anchor="la",
    ):
        self.draw.text(
            (int(x * SCALE), int(y * SCALE)),
            value,
            font=self.font(size, style),
            fill=fill,
            anchor=anchor,
        )

    def text_width(self, value: str, size: float, style: str = "regular"):
        return self.draw.textlength(
            value,
            font=self.font(size, style),
        ) / SCALE

    def paragraph(
        self,
        x: float,
        y: float,
        value: str,
        size: float,
        width: float,
        style: str = "regular",
        fill=MUTED,
        line_height: float | None = None,
    ):
        font = self.font(size, style)
        words = value.split()
        lines = []
        current = ""
        max_px = width * SCALE
        for word in words:
            candidate = word if not current else f"{current} {word}"
            if self.draw.textlength(candidate, font=font) <= max_px:
                current = candidate
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
        line_height = line_height or size * 1.45
        for index, line in enumerate(lines):
            self.text(x, y + index * line_height, line, size, style, fill)
        return y + len(lines) * line_height

    def grid(self, step: float = 72, alpha: int = 18):
        layer = Image.new(
            "RGBA",
            (self.w * SCALE, self.h * SCALE),
            (0, 0, 0, 0),
        )
        draw = ImageDraw.Draw(layer)
        for x in range(0, self.w + 1, int(step)):
            draw.line(
                (x * SCALE, 0, x * SCALE, self.h * SCALE),
                fill=(98, 108, 112, alpha),
                width=SCALE,
            )
        for y in range(0, self.h + 1, int(step)):
            draw.line(
                (0, y * SCALE, self.w * SCALE, y * SCALE),
                fill=(98, 108, 112, alpha),
                width=SCALE,
            )
        self.img.alpha_composite(layer)

    def overlay_rect(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        radius: float,
        fill: tuple,
    ):
        layer = Image.new(
            "RGBA",
            (self.w * SCALE, self.h * SCALE),
            (0, 0, 0, 0),
        )
        draw = ImageDraw.Draw(layer)
        draw.rounded_rectangle(
            (
                int(x * SCALE),
                int(y * SCALE),
                int((x + w) * SCALE),
                int((y + h) * SCALE),
            ),
            radius=int(radius * SCALE),
            fill=fill,
        )
        self.img.alpha_composite(layer)

    def glow(self, center, radius: float, color: tuple, alpha: int = 40):
        layer = Image.new(
            "RGBA",
            (self.w * SCALE, self.h * SCALE),
            (0, 0, 0, 0),
        )
        draw = ImageDraw.Draw(layer)
        cx, cy = center
        draw.ellipse(
            (
                int((cx - radius) * SCALE),
                int((cy - radius) * SCALE),
                int((cx + radius) * SCALE),
                int((cy + radius) * SCALE),
            ),
            fill=(*color, alpha),
        )
        layer = layer.filter(ImageFilter.GaussianBlur(int(radius * 0.55 * SCALE)))
        self.img.alpha_composite(layer)

    def image_cover(
        self,
        path: Path,
        x: float,
        y: float,
        w: float,
        h: float,
        radius: float = 0,
    ):
        with Image.open(path) as source:
            source = source.convert("RGB")
            target_ratio = w / h
            source_ratio = source.width / source.height
            if source_ratio > target_ratio:
                new_h = source.height
                new_w = round(source.height * target_ratio)
                left = (source.width - new_w) // 2
                source = source.crop((left, 0, left + new_w, new_h))
            else:
                new_w = source.width
                new_h = round(source.width / target_ratio)
                top = (source.height - new_h) // 2
                source = source.crop((0, top, new_w, top + new_h))
            target_size = (int(w * SCALE), int(h * SCALE))
            source = source.resize(target_size, Image.Resampling.LANCZOS)
            mask = Image.new("L", target_size, 0)
            mask_draw = ImageDraw.Draw(mask)
            mask_draw.rounded_rectangle(
                (0, 0, target_size[0], target_size[1]),
                radius=int(radius * SCALE),
                fill=255,
            )
            self.img.paste(
                source.convert("RGBA"),
                (int(x * SCALE), int(y * SCALE)),
                mask,
            )

    def pill(
        self,
        x: float,
        y: float,
        label: str,
        fill=PANEL_ALT,
        color=MUTED,
        border=BORDER,
        size=10,
    ):
        width = self.text_width(label, size, "mono") + 24
        self.rect(x, y, width, 28, 14, fill, border, 1)
        self.text(x + 12, y + 14, label, size, "mono", color, "lm")
        return x + width

    def button(
        self,
        x: float,
        y: float,
        label: str,
        primary=True,
        width: float | None = None,
    ):
        width = width or self.text_width(label, 12, "mono-bold") + 42
        fill = ORANGE if primary else (0, 0, 0, 0)
        border = ORANGE if primary else BORDER
        color = BG if primary else TEXT
        self.rect(x, y, width, 46, 4, fill, border, 1.2)
        self.text(
            x + width / 2,
            y + 23,
            label,
            12,
            "mono-bold",
            color,
            "mm",
        )
        return x + width

    def save(self, name: str):
        OUT.mkdir(parents=True, exist_ok=True)
        final = self.img.convert("RGB").resize(
            (self.w, self.h),
            Image.Resampling.LANCZOS,
        )
        path = OUT / name
        final.save(path, quality=95)
        print(path)


def draw_nav(canvas: Canvas, mobile=False):
    if mobile:
        canvas.rect(0, 0, 390, 64, 0, BG)
        canvas.line([(0, 64), (390, 64)], BORDER, 1)
        canvas.text(24, 22, "ZT / PORTFOLIO", 10, "mono-bold", ORANGE)
        canvas.text(366, 22, "MENU", 10, "mono", MUTED, "ra")
        return

    canvas.rect(0, 0, 1440, 88, 0, BG)
    canvas.line([(0, 88), (1440, 88)], BORDER, 1)
    canvas.text(96, 39, "ZT / PORTFOLIO", 12, "mono-bold", ORANGE)
    nav = [("WORK", 680), ("EXPERIENCE", 780), ("ABOUT", 930), ("RESEARCH", 1023)]
    for label, x in nav:
        canvas.text(x, 39, label, 11, "mono", MUTED)
    canvas.button(1182, 21, "RESUME ↗", primary=False, width=162)


def draw_hero_desktop(canvas: Canvas):
    draw_nav(canvas)
    canvas.glow((1260, 230), 340, ORANGE, 22)

    canvas.text(96, 146, "SAN DIEGO / CALIFORNIA", 12, "mono-bold", ORANGE)
    canvas.line([(96, 174), (258, 174)], (86, 49, 34, 255), 2)

    canvas.text(96, 202, "ZHAO", 106, "heavy", TEXT)
    canvas.text(96, 302, "TANG", 106, "heavy", TEXT)
    canvas.rect(96, 424, 88, 6, 3, ORANGE)
    canvas.text(96, 456, "Software Engineer · Data & AI Systems", 30, "demi", TEXT)
    canvas.paragraph(
        96,
        512,
        "I build reliable data platforms, measurable AI products, and "
        "production systems that hold up under real load.",
        18,
        660,
        fill=MUTED,
        line_height=29,
    )
    next_x = canvas.button(96, 624, "EXPLORE SELECTED WORK")
    canvas.button(next_x + 14, 624, "DOWNLOAD RESUME", primary=False)
    canvas.text(
        96,
        704,
        "SYSTEMS  /  DATA  /  AI  /  RELIABILITY",
        10,
        "mono",
        DIM,
    )

    canvas.rect(922, 130, 422, 574, 18, (15, 18, 21, 255), BORDER, 1)
    canvas.image_cover(AVATAR, 940, 148, 386, 482, 12)
    canvas.overlay_rect(940, 646, 386, 38, 0, (9, 11, 13, 215))
    canvas.text(956, 665, "ZHAO TANG / SAN DIEGO", 10, "mono", TEXT, "lm")
    canvas.text(1310, 665, "PORTRAIT 01", 9, "mono", ORANGE, "rm")
    canvas.line([(940, 704), (1326, 704)], (255, 106, 61, 180), 2)
    canvas.line([(1326, 704), (1326, 760)], BORDER, 1)
    canvas.text(1310, 742, "BUILD / MEASURE / OPERATE", 9, "mono", DIM, "ra")


def draw_proof_strip(canvas: Canvas, mobile=False):
    if mobile:
        canvas.line([(24, 990), (366, 990)], BORDER, 1)
        metrics = [
            ("100M+", "users supported"),
            ("40%", "lower MTTR"),
            ("0.840", "Hybrid Hit@5"),
            ("12", "publications"),
        ]
        for index, (value, label) in enumerate(metrics):
            col = index % 2
            row = index // 2
            x = 24 + col * 177
            y = 1020 + row * 74
            canvas.text(x, y, value, 26, "bold", TEXT)
            canvas.text(x, y + 36, label, 10, "mono", MUTED)
        return

    canvas.line([(96, 786), (1344, 786)], BORDER, 1)
    metrics = [
        ("100M+", "USERS SUPPORTED BY INTUIT DATA PRODUCTS"),
        ("40%", "LOWER MTTR THROUGH TRACING AND RCA"),
        ("0.840", "HYBRID HIT@5 / GRAPHATLAS BENCHMARK"),
        ("12", "PEER-REVIEWED PUBLICATIONS"),
    ]
    for index, (value, label) in enumerate(metrics):
        x = 96 + index * 312
        if index:
            canvas.line([(x - 26, 816), (x - 26, 920)], BORDER, 1)
        canvas.text(x, 814, value, 34, "bold", TEXT)
        canvas.paragraph(x, 860, label, 9.5, 250, "mono", MUTED, 17)
    canvas.line([(96, 944), (1344, 944)], BORDER, 1)


def draw_project_card(
    canvas: Canvas,
    x: float,
    y: float,
    w: float,
    image_path: Path,
    label: str,
    title: str,
    summary: str,
    metrics: list[str],
    image_height: float = 212,
    compact=False,
):
    h = 456 if not compact else 418
    canvas.rect(x, y, w, h, 12, PANEL, BORDER, 1)
    canvas.image_cover(image_path, x + 12, y + 12, w - 24, image_height, 8)
    canvas.overlay_rect(
        x + 12,
        y + 12,
        w - 24,
        image_height,
        8,
        (0, 0, 0, 36),
    )
    content_y = y + image_height + 34
    canvas.text(x + 26, content_y, label, 10, "mono-bold", ORANGE)
    canvas.text(x + 26, content_y + 25, title, 25, "demi", TEXT)
    canvas.paragraph(
        x + 26,
        content_y + 66,
        summary,
        14,
        w - 52,
        fill=MUTED,
        line_height=21,
    )
    chip_x = x + 26
    for metric in metrics[:3]:
        chip_x = canvas.pill(chip_x, y + h - 68, metric) + 8
    canvas.text(
        x + w - 26,
        y + h - 34,
        "READ CASE STUDY  →",
        9,
        "mono-bold",
        TEXT,
        "ra",
    )


def draw_selected_work_desktop(canvas: Canvas):
    canvas.text(96, 1000, "01 / SELECTED WORK", 11, "mono-bold", ORANGE)
    canvas.text(96, 1038, "Systems built for evidence,", 48, "demi", TEXT)
    canvas.text(96, 1090, "not just demos.", 48, "demi", TEXT)
    canvas.paragraph(
        920,
        1050,
        "Streaming infrastructure, retrieval engineering, governed "
        "analytics, and scientific computing—with measured outcomes and "
        "explicit boundaries.",
        14,
        424,
        fill=MUTED,
        line_height=22,
    )

    card_w = 612
    draw_project_card(
        canvas,
        96,
        1178,
        card_w,
        CLICKSTREAM,
        "STREAMING DATA PLATFORM",
        "Clickstream",
        "An end-to-end streaming platform that turns high-volume events into "
        "monitored, queryable data products.",
        ["~100 ev/s", "p95 181 ms", "111 tests"],
    )
    draw_project_card(
        canvas,
        732,
        1178,
        card_w,
        GRAPHATLAS,
        "GRAPH RAG / RETRIEVAL",
        "GraphAtlas",
        "A multi-engine knowledge platform with traceable citations and an "
        "evaluation harness that makes retrieval quality measurable.",
        ["0.840 Hit@5", "537 ms p95", "4.38 faithfulness"],
    )
    draw_project_card(
        canvas,
        96,
        1660,
        card_w,
        NL2SQL,
        "GOVERNED AI ANALYTICS",
        "NL2SQLAgent",
        "A natural-language interface to a million-row warehouse, designed "
        "so generated SQL stays inspectable and read-only.",
        ["1.03M rows", "<250 ms", "81 + 51 tests"],
    )
    draw_project_card(
        canvas,
        732,
        1660,
        card_w,
        NANOTRACK,
        "RESEARCH DATA INFRASTRUCTURE",
        "nanotrack",
        "A scientific video-tracking pipeline rebuilt from MATLAB into a "
        "reproducible Python system with orchestration and CI.",
        ["15 h → 30 min", "12 papers", "10k frames"],
    )

    canvas.line([(96, 2170), (1344, 2170)], BORDER, 1)
    canvas.text(96, 2208, "LET’S BUILD SOMETHING", 11, "mono-bold", ORANGE)
    canvas.text(96, 2238, "that can be trusted after launch.", 32, "demi", TEXT)
    canvas.text(
        1344,
        2241,
        "ztangintuit@gmail.com  ↗",
        13,
        "mono",
        TEXT,
        "ra",
    )


def desktop_home():
    canvas = Canvas(1440, 2320)
    canvas.grid()
    draw_hero_desktop(canvas)
    draw_proof_strip(canvas)
    draw_selected_work_desktop(canvas)
    canvas.save("home-desktop.png")


def mobile_home():
    canvas = Canvas(390, 2220)
    canvas.grid(60, 14)
    draw_nav(canvas, mobile=True)
    canvas.glow((330, 330), 190, ORANGE, 20)

    canvas.text(24, 100, "SAN DIEGO / CALIFORNIA", 10, "mono-bold", ORANGE)
    canvas.text(24, 132, "ZHAO", 64, "heavy", TEXT)
    canvas.text(24, 192, "TANG", 64, "heavy", TEXT)
    canvas.rect(24, 270, 62, 5, 3, ORANGE)
    canvas.text(24, 296, "Software Engineer", 23, "demi", TEXT)
    canvas.text(24, 326, "Data & AI Systems", 23, "demi", TEXT)
    canvas.paragraph(
        24,
        376,
        "Reliable data platforms, measurable AI products, and production "
        "systems that hold up under real load.",
        15,
        340,
        fill=MUTED,
        line_height=22,
    )
    canvas.button(24, 474, "EXPLORE WORK", width=164)
    canvas.button(198, 474, "RESUME ↗", primary=False, width=118)

    canvas.rect(24, 552, 342, 430, 14, PANEL, BORDER, 1)
    canvas.image_cover(AVATAR, 36, 564, 318, 398, 8)
    canvas.overlay_rect(36, 924, 318, 42, 0, (9, 11, 13, 220))
    canvas.text(50, 946, "DATA / AI / RELIABILITY", 9, "mono", TEXT, "lm")
    canvas.text(342, 946, "01", 9, "mono", ORANGE, "rm")

    draw_proof_strip(canvas, mobile=True)
    canvas.text(24, 1170, "01 / SELECTED WORK", 10, "mono-bold", ORANGE)
    canvas.text(24, 1201, "Systems built", 39, "demi", TEXT)
    canvas.text(24, 1244, "for evidence,", 39, "demi", TEXT)
    canvas.text(24, 1287, "not demos.", 39, "demi", TEXT)

    draw_project_card(
        canvas,
        24,
        1372,
        342,
        CLICKSTREAM,
        "STREAMING DATA PLATFORM",
        "Clickstream",
        "High-volume events become monitored, queryable data products.",
        ["~100 ev/s", "p95 181 ms", "111 tests"],
        image_height=164,
        compact=True,
    )
    draw_project_card(
        canvas,
        24,
        1812,
        342,
        GRAPHATLAS,
        "GRAPH RAG / RETRIEVAL",
        "GraphAtlas",
        "Multi-engine retrieval with traceable citations and measurable quality.",
        ["0.840 Hit@5", "537 ms", "4.38 faithfulness"],
        image_height=164,
        compact=True,
    )
    canvas.save("home-mobile.png")


def architecture_box(canvas, x, y, w, h, label, detail, accent=ORANGE):
    canvas.rect(x, y, w, h, 6, PANEL_ALT, BORDER, 1)
    canvas.rect(x, y, 5, h, 2, accent)
    canvas.text(x + 20, y + 26, label, 15, "demi", TEXT)
    canvas.text(x + 20, y + 54, detail, 9, "mono", MUTED)


def case_study():
    canvas = Canvas(1440, 2050)
    canvas.grid()
    draw_nav(canvas)
    canvas.glow((1180, 360), 300, ORANGE, 18)

    canvas.text(96, 148, "CASE STUDY / CLICKSTREAM", 11, "mono-bold", ORANGE)
    canvas.text(96, 190, "Real-time events.", 67, "heavy", TEXT)
    canvas.text(96, 260, "Operable data products.", 67, "heavy", TEXT)
    canvas.paragraph(
        96,
        360,
        "A production-shaped pipeline built to test the full path from event "
        "generation to a monitored read API—and the boundary between a "
        "portfolio system and production traffic.",
        17,
        760,
        fill=MUTED,
        line_height=27,
    )
    canvas.pill(96, 470, "KAFKA")
    canvas.pill(180, 470, "SPARK")
    canvas.pill(274, 470, "POSTGRESQL")
    canvas.pill(412, 470, "CLICKHOUSE")
    canvas.pill(554, 470, "FASTAPI")

    stats = [
        ("~100 / s", "producer throughput"),
        ("p95 180.6 ms", "k6 load test"),
        ("111", "python tests passing"),
    ]
    for index, (value, label) in enumerate(stats):
        x = 96 + index * 420
        canvas.rect(x, 546, 392, 110, 8, PANEL, BORDER, 1)
        canvas.text(x + 24, 576, value, 29, "bold", TEXT)
        canvas.text(x + 24, 620, label, 9.5, "mono", MUTED)

    canvas.text(96, 714, "ARCHITECTURE / EVENT TO API", 11, "mono-bold", ORANGE)
    canvas.rect(96, 750, 1248, 440, 12, (15, 18, 21, 255), BORDER, 1)
    mini_w, mini_h, row1, row2 = 194, 92, 820, 1010
    architecture_box(canvas, 142, row1, mini_w, mini_h, "PRODUCER", "~100 events / s")
    architecture_box(canvas, 374, row1, mini_w, mini_h, "KAFKA", "clicks.raw + DLQ")
    architecture_box(canvas, 606, row1, mini_w, mini_h, "SPARK", "1-min windows")
    architecture_box(canvas, 838, row1, mini_w, mini_h, "POSTGRES", "curated aggregates")
    architecture_box(canvas, 1070, row1, mini_w, mini_h, "CLICKHOUSE", "analytics store")
    architecture_box(canvas, 606, row2, mini_w, mini_h, "FASTAPI", "read-only API")
    architecture_box(canvas, 838, row2, mini_w, mini_h, "PROM / GRAFANA", "SLIs + alerts")
    architecture_box(canvas, 1070, row2, mini_w, mini_h, "AIRFLOW / DBT", "quality + rollups")
    for x1, x2 in [(336, 374), (568, 606), (800, 838), (1032, 1070)]:
        canvas.line([(x1, 866), (x2, 866)], ORANGE, 2)
        canvas.line([(x2 - 7, 861), (x2, 866), (x2 - 7, 871)], ORANGE, 2)
    canvas.line([(703, 912), (703, 1010)], ORANGE, 2)
    canvas.line([(703, 961), (838, 961), (838, 1010)], ORANGE, 2)
    canvas.line([(935, 912), (935, 961), (1070, 961), (1070, 1010)], ORANGE, 2)
    canvas.text(1190, 1138, "SYNTHETIC TRAFFIC / LOCAL + KIND MEASUREMENTS", 9, "mono", DIM, "ra")

    canvas.text(96, 1252, "EVIDENCE / WHAT HELD UNDER TEST", 11, "mono-bold", ORANGE)
    evidence = [
        ("0%", "errors", "3,227 requests at ~46 req/s"),
        ("21 s", "API recovery", "pod-deletion chaos drill"),
        ("33 s", "Kafka recovery", "broker-loss chaos drill"),
    ]
    for index, (value, label, detail) in enumerate(evidence):
        x = 96 + index * 420
        canvas.rect(x, 1292, 392, 188, 8, PANEL, BORDER, 1)
        canvas.text(x + 24, 1328, value, 38, "bold", ORANGE)
        canvas.text(x + 24, 1379, label.upper(), 10, "mono-bold", TEXT)
        canvas.text(x + 24, 1412, detail, 10, "mono", MUTED)

    canvas.text(96, 1530, "PRODUCT EVIDENCE / LIVE OPERATIONS VIEW", 11, "mono-bold", ORANGE)
    canvas.image_cover(CLICKSTREAM, 96, 1568, 1248, 300, 10)
    canvas.overlay_rect(96, 1568, 1248, 300, 10, (0, 0, 0, 40))
    canvas.rect(96, 1872, 1248, 1, 0, BORDER)
    canvas.text(96, 1900, "LIMITATIONS", 10, "mono-bold", ORANGE)
    canvas.paragraph(
        200,
        1894,
        "Synthetic events, short-run measurements, and single-node Kafka. "
        "Production-shaped engineering—not production traffic.",
        13,
        1080,
        fill=MUTED,
        line_height=21,
    )
    canvas.text(1344, 1972, "VIEW ON GITHUB  →", 11, "mono-bold", TEXT, "ra")
    canvas.save("case-study-desktop.png")


if __name__ == "__main__":
    desktop_home()
    mobile_home()
    case_study()
