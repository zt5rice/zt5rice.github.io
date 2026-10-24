#!/usr/bin/env python3
"""Generate the 1200x630 Open Graph preview image."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "public/assets/portfolio/avatar/zhao-tang-portrait.webp"
OUTPUT = ROOT / "public/og/og-portfolio.png"
SCALE = 2

BG = (9, 11, 13)
TEXT = (242, 238, 230)
MUTED = (158, 163, 166)
DIM = (111, 118, 122)
ORANGE = (255, 106, 61)
BORDER = (43, 47, 50)

AVENIR = "/System/Library/Fonts/Avenir Next.ttc"
MENLO = "/System/Library/Fonts/Menlo.ttc"


def font(size: int, kind: str = "regular"):
    if kind == "heavy":
        return ImageFont.truetype(AVENIR, size * SCALE, index=8)
    if kind == "medium":
        return ImageFont.truetype(AVENIR, size * SCALE, index=5)
    if kind == "mono":
        return ImageFont.truetype(MENLO, size * SCALE, index=0)
    if kind == "mono-bold":
        return ImageFont.truetype(MENLO, size * SCALE, index=1)
    return ImageFont.truetype(AVENIR, size * SCALE, index=7)


def draw_text(draw, xy, value, size, kind="regular", fill=TEXT):
    draw.text(
        (xy[0] * SCALE, xy[1] * SCALE),
        value,
        font=font(size, kind),
        fill=fill,
    )


def main() -> None:
    canvas = Image.new("RGB", (1200 * SCALE, 630 * SCALE), BG)
    draw = ImageDraw.Draw(canvas)

    for x in range(0, 1200, 60):
        draw.line(
            (x * SCALE, 0, x * SCALE, 630 * SCALE),
            fill=(21, 25, 28),
            width=SCALE,
        )
    for y in range(0, 630, 60):
        draw.line(
            (0, y * SCALE, 1200 * SCALE, y * SCALE),
            fill=(21, 25, 28),
            width=SCALE,
        )

    draw.rectangle(
        (72 * SCALE, 50 * SCALE, 102 * SCALE, 80 * SCALE),
        outline=ORANGE,
        width=2 * SCALE,
    )
    draw_text(draw, (87, 65), "ZT", 13, "mono-bold", ORANGE)
    draw_text(draw, (120, 56), "PORTFOLIO / DATA & AI SYSTEMS", 12, "mono", MUTED)
    draw_text(draw, (72, 116), "SAN DIEGO / CALIFORNIA", 12, "mono-bold", ORANGE)
    draw_text(draw, (72, 150), "Dr. Zhao", 68, "heavy", TEXT)
    draw_text(draw, (72, 218), "Tang", 68, "heavy", TEXT)
    draw.rectangle((72 * SCALE, 298 * SCALE, 142 * SCALE, 304 * SCALE), fill=ORANGE)
    draw_text(
        draw,
        (72, 332),
        "Software Engineer · Data & AI Systems",
        27,
        "medium",
        TEXT,
    )
    draw_text(
        draw,
        (72, 382),
        "Reliable data platforms. Measurable AI products.",
        20,
        "regular",
        MUTED,
    )
    draw_text(
        draw,
        (72, 412),
        "Production systems built to hold up under load.",
        20,
        "regular",
        MUTED,
    )

    metrics = [
        ("100M+", "users supported"),
        ("40%", "lower MTTR"),
        ("0.840", "Hybrid Hit@5"),
        ("6", "publications"),
    ]
    for index, (value, label) in enumerate(metrics):
        x = 72 + index * 138
        draw_text(draw, (x, 484), value, 29, "medium", TEXT)
        draw_text(draw, (x, 522), label.upper(), 9, "mono", MUTED)

    portrait = Image.open(SOURCE).convert("RGB")
    target_ratio = 280 / 340
    source_ratio = portrait.width / portrait.height
    if source_ratio > target_ratio:
        crop_width = round(portrait.height * target_ratio)
        left = (portrait.width - crop_width) // 2
        portrait = portrait.crop((left, 0, left + crop_width, portrait.height))
    else:
        crop_height = round(portrait.width / target_ratio)
        top = (portrait.height - crop_height) // 2
        portrait = portrait.crop((0, top, portrait.width, top + crop_height))
    portrait = portrait.resize((280 * SCALE, 340 * SCALE), Image.Resampling.LANCZOS)

    mask = Image.new("L", portrait.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        (0, 0, portrait.width, portrait.height),
        radius=14 * SCALE,
        fill=255,
    )
    canvas.paste(portrait, (820 * SCALE, 130 * SCALE), mask)
    draw.rounded_rectangle(
        (806 * SCALE, 116 * SCALE, 1114 * SCALE, 484 * SCALE),
        radius=20 * SCALE,
        outline=BORDER,
        width=2 * SCALE,
    )
    draw_text(draw, (836, 445), "Dr. Zhao Tang / San Diego", 9, "mono", TEXT)
    draw_text(draw, (1090, 445), "PORTRAIT 01", 8, "mono", ORANGE)
    site_label = "zt5rice.github.io"
    site_width = draw.textlength(site_label, font=font(10, "mono")) / SCALE
    draw_text(draw, (1128 - site_width, 574), site_label, 10, "mono", DIM)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.resize((1200, 630), Image.Resampling.LANCZOS).save(OUTPUT, quality=95)
    print(OUTPUT)


if __name__ == "__main__":
    main()
