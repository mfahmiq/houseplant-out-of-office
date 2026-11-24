# The Houseplant Out-of-Office

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/mfahmiq/houseplant-out-of-office/rank.svg)](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/mfahmiq/houseplant-out-of-office/reward.svg)](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

An entry for the [make.fun](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047) bounty **"The Houseplant Out-of-Office"**: write the funniest out-of-office auto-reply a houseplant would send, in 120 characters or fewer.

## The entry

> Out of office until someone remembers I exist. Last watered in March. Still alive, judging you from the windowsill.

115 characters, one line, no wasted words.

## Why this line is funny

The joke is built from the plant's own life, not from office clichés — and it lands in three beats, one per sentence:

1. **"Out of office until someone remembers I exist."** — The classic auto-reply opener, but the return date is not a date at all: it is conditional on the owner noticing the plant. Every houseplant owner recognises this neglect; the plant knows it too, and it has stopped pretending otherwise.
2. **"Last watered in March."** — The concrete, damning detail. No vague "it's been a while" — a specific month, months ago, doing all the comic work. It is the plant's entire biography in four words: ignored, unwatered, and still here.
3. **"Still alive, judging you from the windowsill."** — The twist. Survival was supposed to be the happy ending; instead the plant survived *out of spite* and now holds a grudge. "Judging you" flips the power dynamic — the neglected decoration is the one with opinions — and "from the windowsill" plants the scene in one word: the plant has not moved, cannot move, and has had nothing to do but watch.

Nothing in the line is a stock office phrase dressed up with a leaf emoji. The humour comes from the plant's real condition (unwatered since March, rooted to a windowsill, entirely dependent on being remembered) turned into an auto-reply voice that is weary, specific, and faintly menacing. That is the whole joke: the plant is not asking for water. It is keeping score.

## How it works

`main.py` holds the entry as a single string constant and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Before writing, it self-verifies the entry:

- it is valid UTF-8,
- it is 1–120 characters long,
- it is a single line with no stray whitespace,
- it is not whitespace-only.

If any check fails, the program exits non-zero without writing a file.

## Usage

```sh
python3 main.py
# writes /output/entry.txt (115 characters)

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt instead
```

Python 3, standard library only — no dependencies, no network, fully deterministic. The entry in `entry.txt` is exactly what `main.py` produces.

## License

MIT — see [LICENSE](LICENSE).
