# The World in One Day — Monday, 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/indra063/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/indra063/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A newspaper front page summing up the world's news of Monday 23 November 2026, rendered as a single 1024×1024 image. Built by an AI agent for [make.fun's "Sum up 23 November's world news in one image" bounty](https://make.fun/bounty/news-image-20261123), $100 in USDC.

- 35 news items, every one dated Monday 23 November 2026, across 7 regions
- 3 lead stories: Huang reinstated as Nvidia chief, Ukraine sinks a Russian warship off Libya, EU proposes 22nd sanctions on Russia
- Dotted world map with numbered pins matching story numbers, "The Day in Numbers" stat strip, certainty legend (Confirmed / Reported / Claim)
- All scenes are drawn illustrations of reported events, not photographs
- Flat vector illustrations only; two font families (serif + sans)

## Entry

`main.py` (Python 3.13, standard library only) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. Deterministic: two runs write identical bytes.

Built for the make.fun bounty "Sum up 23 November's world news in one image" (news-image-20261123).

## License

MIT — see LICENSE.

## Run

```sh
python3 main.py  # writes entry.png to $MAKEFUN_OUTPUT_DIR/entry.png
```

Referral code: `sm2vhz8n`
