#!/usr/bin/env python3
"""Add meme captions to the generated GTA 6 base image.

Top caption in the sky, bottom punchline in the sand, both in bold
white letters with a thick black outline so they stay readable when
the picture is shrunk to 480x480.
"""
from PIL import Image, ImageDraw, ImageFont

SRC = "assets/media-generation-meme-base-0-c1326839-16f7-4981-924b-b05109138ab3.png"
DST = "meme.png"

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def outlined_text(draw, cx, y, text, font, fill="white", outline="black", width=6):
    """Draw centred text with a thick outline."""
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    x = cx - w // 2
    draw.text((x, y), text, font=font, fill=fill,
              stroke_width=width, stroke_fill=outline)


def fit_font(text, max_width, start_size):
    size = start_size
    while size > 20:
        font = ImageFont.truetype(BOLD, size)
        if font.getlength(text) <= max_width:
            return font
        size -= 4
    return ImageFont.truetype(BOLD, size)


def main():
    img = Image.open(SRC).convert("RGB")
    w, h = img.size
    draw = ImageDraw.Draw(img)

    top1 = fit_font("ME CALLING IN SICK", int(w * 0.92), 92)
    top2 = fit_font("FOR GTA 6 LAUNCH DAY", int(w * 0.92), 92)
    outlined_text(draw, w // 2, 30, "ME CALLING IN SICK", top1)
    outlined_text(draw, w // 2, 30 + top1.size + 12, "FOR GTA 6 LAUNCH DAY", top2)

    bottom = fit_font("SINCE 2013", int(w * 0.8), 130)
    outlined_text(draw, w // 2, h - bottom.size - 150, "SINCE 2013", bottom, width=8)

    brand = ImageFont.truetype(BOLD, 54)
    outlined_text(draw, w // 2, h - 78, "make.fun", brand,
                  fill="#ff2e88", outline="white", width=4)

    img.save(DST, "PNG")
    print(f"saved {DST} {img.size}")


if __name__ == "__main__":
    main()
