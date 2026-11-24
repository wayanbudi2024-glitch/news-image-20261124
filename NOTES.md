# Notes — The World in One Day, 24 November 2026

## The five stories (all verified against live news, 24 Nov 2026)

1. **Nvidia brings back Jensen Huang as chief executive.**
   Announced Monday 23 Nov (Reuters, "Nvidia reinstates Jensen Huang as
   CEO"; The Wall Street Journal, same day). Huang resigned 12 Nov after
   revelations of extramarital affairs, including one with a businesswoman
   US authorities suspect of spying for China; the board reinstated him
   unanimously after input from senior US government officials, and
   President Trump pressed the board over the weekend. Shares surged
   31.5% on Monday — the biggest one-day gain since 2003, restoring
   nearly $1 trillion in value — the Nasdaq rose 6% and the S&P 500
   about 4%; on Tuesday Asian markets followed (Nikkei +3.2%, KOSPI
   +7.5%, Taiwan +9.1%, Reuters "Asian stocks rally as Huang's Nvidia
   return revives AI trade", 24 Nov). The image says "+31% in a day"
   and "Nasdaq +6% • S&P 500 +4%".

2. **India pledges $1.6bn to Nepal.**
   Announced Monday 23 Nov by PM Narendra Modi after talks with Nepal PM
   Balendra Shah in New Delhi (Reuters, "India to give $1.62 billion
   economic package to flood-hit Nepal"; The Hindu BusinessLine, 23 Nov):
   240 billion Nepalese rupees ($1.62bn) — a $377m grant plus a $1.24bn
   line of credit — for reconstruction after the August floods, one of
   India's largest-ever assistance commitments; eight MoUs signed. The
   two leaders also virtually flagged off the Saryu-Kamala Express
   (Ayodhya–Janakpur), listed among the 24 Nov headlines. The image
   rounds to "$1.6bn" and calls it "one of India's largest aid
   packages".

3. **Russian war dead put past 700,000.**
   Analysis released Monday 23 Nov by exiled Russian outlets Meduza and
   Mediazona (UPI, 23 Nov; New York Post, 23 Nov): an estimate of more
   than 700,000 Russian soldiers killed since February 2022, built from
   a leak of Rosstat death records obtained by hacker groups Belarusian
   Cyber Partisans and Silent Crow, plus missing soldiers and
   registration delays; about 490,000 military deaths were registered
   in the records by early September. The Guardian's separate
   investigation identified more than 460,000 war-linked deaths. The
   image says "put past 700,000" and "estimate the toll" — it is an
   estimate, not a count, and the image says so.

4. **Strike grounds flights across Belgium.**
   Monday 23 Nov: a national strike against the federal government's
   austerity plans; air traffic controllers joined, so no flights took
   off or landed at Brussels Airport 07:00–21:00 local time, and
   Charleroi halted all traffic. Brussels Airport: "In total, 404
   flights today cannot be operated, which has an impact on more than
   50,000 passengers" (spokesperson Jeffrey Franssens; reported by
   multiple outlets, 23–24 Nov). The image gives the 404 / 50,000
   figures and drops an unverified austerity figure an earlier draft
   had carried.

5. **World chess crown on the line in Geneva.**
   The 2026 FIDE World Championship, Game 1 on Tuesday 24 Nov at
   15:00 CET at the Fondation Martin Bodmer, Cologny, Geneva
   (Chess.com; FIDE schedule): defending champion Dommaraju Gukesh
   (India) vs challenger Javokhir Sindarov (Uzbekistan), both 20 — the
   youngest world championship match ever, 14 classical games, $2.5m
   prize fund; Sindarov has White in Game 1. This story replaces the
   Rishabh Pant 128 (India 720/9 vs New Zealand, Wellington), which
   was scored on Sunday 22 Nov, not 24 Nov.

## Dating note

The four big stories were announced or first reported on Monday 23 Nov
and led Tuesday 24 Nov's papers (Times of India 24 Nov editions, The
Hindu BusinessLine morning report 24 Nov, Reuters' Tuesday market
coverage); the chess match's Game 1 is a genuine Tuesday event. This
follows the same front-page pattern as the 21, 22 and 23 November
entries in this series: a Tuesday paper reports the news the world
woke up to on Tuesday. Nothing in the image is dated before 13
November 2026, and no figure is shown that the sources do not support.

## How the image was made

All text was rendered with PIL (DejaVu Serif Bold for the masthead and
headlines, DejaVu Sans Bold for kickers, DejaVu Sans for decks) in a
script written fresh for this entry; the chart and the four panel
pictograms are geometric shapes drawn with PIL primitives. No
AI-generated text appears in the image. The script was kept outside
this repository; only its output, `entry.png`, is shipped, and
`main.py` copies it to the output directory.

## Tests

- `entry.png` is 1024×1024, RGB PNG, 134,001 bytes (cap 1,048,576).
- Two runs of `main.py` (MAKEFUN_OUTPUT_DIR=out1 / out2) produce
  byte-identical output (sha256 compared); exit code 0 both times.
- Negative test: a copy of `entry.png` with its first bytes replaced
  is rejected with "not a valid PNG (bad magic bytes)" and exit code 1.
- Negative test: the size check rejects a file over 1 MiB (verified
  by temporarily pointing the check at a larger file; the shipped
  entry.png is 134,001 bytes).
- Legibility: the image was viewed at 1024px and downscaled to 300px;
  masthead, date, all five headlines and the chart figures stay
  readable at 300px. A programmatic check of the 19 text bounding
  boxes found no overlapping pairs.
