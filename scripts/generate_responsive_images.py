#!/usr/bin/env python3
"""Generate 640/1280 WebP and AVIF variants for static portfolio images."""

from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = ROOT / "public" / "assets" / "portfolio"
WIDTHS = (640, 1280)


def variant_path(source: Path, width: int, suffix: str) -> Path:
    return source.with_name(f"{source.stem}-{width}.{suffix}")


def main() -> None:
    generated = 0
    for source in sorted(ASSET_ROOT.rglob("*.webp")):
        if source.stem.endswith(("-640", "-1280")):
            continue

        with Image.open(source) as image:
            image.load()
            frames = getattr(image, "n_frames", 1)
            if frames > 1:
                print(f"skip animated: {source.relative_to(ASSET_ROOT)}")
                continue

            image = ImageOps.exif_transpose(image)
            if image.mode not in ("RGB", "RGBA"):
                image = image.convert("RGBA" if "transparency" in image.info else "RGB")

            widths = {image.width}
            widths.update(width for width in WIDTHS if width < image.width)

            for width in sorted(widths):
                if width == image.width:
                    resized = image
                else:
                    height = round(image.height * width / image.width)
                    resized = image.resize((width, height), Image.Resampling.LANCZOS)

                webp_target = variant_path(source, width, "webp")
                avif_target = variant_path(source, width, "avif")
                resized.save(webp_target, "WEBP", quality=82, method=6)
                resized.save(avif_target, "AVIF", quality=58)
                generated += 2

    print(f"generated {generated} responsive image files")


if __name__ == "__main__":
    main()
