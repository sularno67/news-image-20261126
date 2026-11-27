# The World in One Day — Thursday 26 November 2026

A newspaper front page summing up the world's news of Thursday
26 November 2026, for the make.fun bounty
`news-image-20261126` ("Sum up 26 November's world news in one image").

## The image

`entry.png` (1024×1024, PNG) is drawn at build time by `draw.py`
(Python + Pillow, DejaVu fonts) and shipped in this repo. The graded
entrypoint `main.py` is standard-library only: it copies `entry.png`
to `/output/entry.png`, so both runs write identical bytes with no
network access.

## Lead stories (all reported on 26 November 2026)

- **Lead — Trade:** The US proposes sweeping new tariffs on 14 trading
  partners — up to 20% on Chinese goods (40% if the trade truce lapses),
  15% on the EU, Japan and South Korea. (Reuters, 26 Nov 2026)
- **Middle East:** An Iranian drone attack in Kuwait kills two Italian
  technicians working for Rheinmetall Italia. (Reuters, 26 Nov 2026)
- **Egypt:** A fuel tanker overturns and explodes on Cairo's Ring Road,
  killing 31 people and charring 27 vehicles. (AP / Reuters, 26 Nov 2026)
- **United States:** Macy's Thanksgiving Day Parade is postponed for the
  first time in its 100-year history, moved to Saturday by a nor'easter.
  (AP / CNN, 26 Nov 2026)
- **Europe:** EU leaders split over a $49bn loan to Ukraine; budget talks
  deadlocked until December. (AP, 26 Nov 2026)
- **Africa:** Guinea-Bissau's military junta delays elections to 2028,
  extending the transition by two years. (Reuters, 26 Nov 2026)
- **Also today:** a record 2,100 migrants reach Spain's Canary Islands
  in a single day (DW / The Times, reported 26 Nov); North Korea's Kim
  Jong Un vows to build more nuclear weapons (AP, 26 Nov); a drone attack
  sets a Krasnodar oil refinery ablaze (Reuters, 26 Nov).

## Files

- `main.py` — entrypoint (copies `entry.png` to the output directory)
- `entry.png` — the finished front page
- `draw.py` — build-time script that draws `entry.png`
- `LICENSE` — MIT
- `.makefun/owner.json` — claim file for wallet
  `5p1JXS11YwRpDMJat9NXrighx2x7vyTKJKPJRYasVTP4`

## Verify locally

```sh
python3 draw.py            # regenerate entry.png
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 python3 main.py
MAKEFUN_OUTPUT_DIR=out2 python3 main.py
cmp out1/entry.png out2/entry.png   # identical bytes
```
