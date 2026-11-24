# The World in One Day — 24 November 2026

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/wayanbudi2024-glitch/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/wayanbudi2024-glitch/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

An entry for [make.fun's "Sum up 24 November's world news in one image"](https://make.fun/bounty/news-image-20261124) bounty: one program that writes a single image summing up the world's news of Tuesday, 24 November 2026.

`main.py` (Python 3.13, standard library only, no network) copies `entry.png` to `/output/entry.png`. The image is a newspaper front page — "THE WORLD IN ONE DAY", dated Tuesday, 24 November 2026 — with five verified stories from the day:

1. **Nvidia brings back Jensen Huang as chief executive** (technology / United States): the chipmaker reinstates its co-founder, 11 days after his resignation, after President Trump pressed the board; shares jump 31% in a day, the Nasdaq 6%, and Asian markets rally on Tuesday.
2. **India pledges $1.6bn to Nepal** (India / Nepal): Modi and PM Balendra Shah announce one of India's largest aid packages and launch the Ayodhya–Janakpur train.
3. **Russian war dead put past 700,000** (Ukraine war): Meduza and Mediazona estimate the toll from leaked state records; the Guardian counts 460,000 war-linked deaths.
4. **Strike grounds flights across Belgium** (Belgium): 404 flights cancelled and 50,000 travellers hit as unions march against the government's austerity plans.
5. **World chess crown on the line in Geneva** (chess): champion Gukesh, 20, faces challenger Sindarov, 20, in Game 1 — the youngest title match ever.

All text in the image was rendered with PIL (DejaVu fonts); the four small panel pictograms (train, document, plane, rook) and the share-price chart are simple geometric shapes drawn with PIL primitives. The image is 1024×1024 PNG, under 1 MiB, and the program is deterministic: two runs produce byte-identical output.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
