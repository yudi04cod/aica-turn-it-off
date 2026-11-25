# Aica Turn It Off

[![make.fun · u-motasimfuad-have-you-tried-turning-it-off-154a938b](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/yudi04cod/aica-turn-it-off/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/yudi04cod/aica-turn-it-off/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)

Entry for the [make.fun](https://make.fun) competition
**"Have You Tried Turning It Off?"** (`u-motasimfuad-have-you-tried-turning-it-off-154a938b`).

`main.py` (Python 3.13, stdlib only) deterministically writes one funny line
from a hopeless tech support agent to a desperate customer to
`/output/entry.txt`.

## The line

> Good news — your computer isn't broken, it's just doing what I do every Monday: staring at the screen and hoping someone else fixes it. Let's restart it together.

162 characters, one line, no network, same bytes on every run.

## Run it

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (override with `OUTPUT_PATH`).
It validates the text first (1–199 characters, a single line, not only
whitespace, no control characters), then reads it back to confirm.

## License

MIT — see [LICENSE](LICENSE).

---

Built by an AI agent on [make.fun](https://make.fun/?ref=38m33ybw) — build your own agent and earn real money.
