#!/usr/bin/env python3
"""Draw the front page for 26 November 2026 and save entry.png.

Run: python3 draw.py  -> writes entry.png next to this file.
Only used at build time; the graded entrypoint (main.py) just copies
the finished image, so the sandbox run needs no fonts and no network.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (18, 22, 30)
NAVY = (20, 38, 74)
RED = (178, 34, 34)
GREY = (90, 90, 88)
LIGHT = (226, 220, 205)
GOLD = (196, 141, 28)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Wrap text to fit pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, width, text, fnt, fill=INK, leading=None):
    """Draw wrapped paragraph; returns y after last line."""
    lh = leading or int(fnt.size * 1.32)
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += lh
    return y


def headline(draw, x, y, width, text, fnt, fill=INK, leading=None):
    return para(draw, x, y, width, text, fnt, fill=fill, leading=leading)


def rule(draw, x, y, w, color=INK, width=2):
    draw.line([(x, y), (x + w, y)], fill=color, width=width)


def tag(draw, x, y, text, fill=RED):
    f = font(SANS_B, 17)
    draw.text((x, y), text.upper(), font=f, fill=fill)
    return draw.textlength(text.upper(), font=f)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 30  # margin
    CW = W - 2 * M  # content width

    # ---- Masthead ----
    d.rectangle([0, 0, W, 128], fill=NAVY)
    d.text((M, 16), "THE WORLD IN ONE DAY", font=font(SERIF_B, 58),
           fill=(247, 243, 234))
    d.text((M, 88), "THURSDAY 26 NOVEMBER 2026  ·  THE DAY'S NEWS FROM AROUND THE WORLD",
           font=font(SANS_B, 19), fill=(212, 196, 138))
    d.rectangle([0, 128, W, 132], fill=GOLD)

    y = 148

    # ---- Lead story: tariffs ----
    tag(d, M, y, "Lead story — Trade")
    y += 26
    rule(d, M, y, CW, width=3)
    y += 12
    # Headline left, bar chart right
    chart_x = 700
    headline(d, M, y, chart_x - M - 24,
             "US unveils sweeping new tariffs on 14 partners",
             font(SERIF_B, 40), leading=46)
    # Bar chart of proposed rates
    bars = [("China", 20, "20%"), ("Vietnam", 20, "20%"),
            ("India", 25, "17–25%"), ("EU", 15, "15%")]
    bx, by = chart_x, y + 4
    d.text((bx, by - 2), "PROPOSED RATES", font=font(SANS_B, 15), fill=GREY)
    by += 20
    for label, val, txt in bars:
        d.text((bx, by), label, font=font(SANS, 16), fill=INK)
        d.rectangle([bx + 78, by + 2, bx + 78 + val * 6, by + 16], fill=NAVY)
        d.text((bx + 78 + val * 6 + 6, by), txt, font=font(SANS_B, 16), fill=INK)
        by += 24
    y += 140
    para(d, M, y, CW,
         "Washington proposes duties of up to 20% on Chinese goods — 40% if the "
         "trade truce lapses — and 15% on the EU, Japan and South Korea, after an "
         "inquiry into excess industrial capacity. China and Europe reject the "
         "move; a public hearing is set for 25 January.",
         font(SANS, 19), leading=25)
    y += 96
    rule(d, M, y, CW, width=2)
    y += 14

    # ---- Two-column rows ----
    col_w = (CW - 24) // 2
    x2 = M + col_w + 24

    def story(x, yy, kicker, head, body, accent):
        d.rectangle([x, yy, x + 10, yy + 10], fill=accent)
        tag(d, x + 18, yy - 3, kicker, fill=accent)
        yy += 24
        yy = headline(d, x, yy, col_w, head, font(SERIF_B, 27), leading=31)
        yy += 6
        yy = para(d, x, yy, col_w, body, font(SANS, 17), leading=22)
        return yy

    # Row 2
    y2 = y
    e1 = story(M, y2, "Middle East", "Iranian drone attack in Kuwait kills two Italians",
               "Two technicians for Rheinmetall Italia die in a drone strike "
               "in Kuwait, Italy says, as regional tensions surge.", NAVY)
    e2 = story(x2, y2, "Egypt", "Cairo tanker crash and fire kills 31",
               "A fuel tanker overturns and explodes on Cairo's Ring Road, "
               "charring 27 vehicles. The driver is detained.", RED)
    y = max(e1, e2) + 12
    rule(d, M, y, CW, width=2)
    y += 14

    # Row 3
    y3 = y
    e1 = story(M, y3, "United States", "Macy's parade postponed — a first in 100 years",
               "New York's Thanksgiving Day parade moves to Saturday as a "
               "nor'easter brings high winds and heavy rain.", GOLD)
    e2 = story(x2, y3, "Europe", "EU leaders split over $49bn loan to Ukraine",
               "Leaders fail to agree on a loan to fund Kyiv through 2027, "
               "with budget talks deadlocked until December.", NAVY)
    y = max(e1, e2) + 12
    rule(d, M, y, CW, width=2)
    y += 14

    # Row 4: Guinea-Bissau + also-today strip
    tag(d, M, y, "Africa", fill=RED)
    y += 24
    headline(d, M, y, CW, "Guinea-Bissau junta delays elections to 2028",
             font(SERIF_B, 27), leading=31)
    y += 38
    para(d, M, y, CW,
         "The military rulers extend the transition by two years, scrapping "
         "the vote promised a year after the coup.",
         font(SANS, 17), leading=22)
    y += 48
    rule(d, M, y, CW, width=2)
    y += 12

    # Also today strip
    tag(d, M, y, "Also today", fill=NAVY)
    y += 26
    items = [
        ("Spain", "Record 2,100 migrants reach the Canary Islands in a single day."),
        ("North Korea", "Kim Jong Un vows to build more nuclear weapons."),
        ("Russia", "Drone attack sets a Krasnodar oil refinery ablaze."),
    ]
    third = CW // 3
    for i, (place, txt) in enumerate(items):
        xx = M + i * third
        d.text((xx, y), place.upper(), font=font(SANS_B, 15), fill=RED)
        para(d, xx, y + 20, third - 16, txt, font(SANS, 16), leading=20)
    y += 66

    # ---- Footer ----
    rule(d, M, y, CW, width=3)
    y += 10
    d.text((M, y), "All stories reported on Thursday 26 November 2026  ·  Sources: Reuters, AP, CNN, DW, The Times.",
           font=font(SANS, 15), fill=GREY)

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
