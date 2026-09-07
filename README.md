# CS Slides — AS 2026-2027

## Start here

Two repos: this one (the lessons) and the vault (the cards behind them).

```bash
mkdir -p ~/AS-CS && cd ~/AS-CS
git clone --depth 1 https://github.com/Kepei-Lei102/the-slides-as.git
git clone --depth 1 https://github.com/Kepei-Lei102/the-vault-as.git
```

The first is instant. The second is about a few hundred MB — a few minutes. If it stops
partway, **don't start over**: `cd` in and run `git pull`, which picks up where
it left off. That is one of the better reasons to be using git at all.

Then double-click any `slides_*.html` to run a deck.

**Every week after a lesson**, new material appears here:

```bash
cd ~/AS-CS/the-slides-as && git pull
```

You'll run that one about thirty times this year.

**Using an AI to drive it?** Good — but ask it to explain as it goes:

> Read https://raw.githubusercontent.com/Kepei-Lei102/the-slides-as/main/SETUP.md and follow it. Explain each git command before you run it.

[`SETUP.md`](SETUP.md) is the long version: what each command does, what to do
when one of them complains, and how to point an AI tutor at the cards.

---

The interactive decks, practice sheets and 🍦 challenges for
**AS Computer Science**, as they are taught. This repo grows through the year: a lesson's
material appears here after that lesson has run.

**This is not everything that exists.** It is everything you have been taught.
If a unit you want is missing, it is because we have not reached it — ask.

## What is in here

| kind | file | how to use it |
|---|---|---|
| deck | `slides_<unit>_*.html` | **double-click it.** It opens in your browser. Arrow keys move; `↓` enters a rabbit hole; the Python cells run live, in the page |
| practice | `practice_<unit>_*.pdf` | print it or annotate it; answers come back in class |
| 🍦 challenge | `Challenge<unit>*.java`, `challenge_<unit>_*.py` | open in an editor, fill in the functions, run the file — the judge is at the bottom and marks itself |

The decks need an internet connection the first time you open one: they pull
Reveal.js and Pyodide from a CDN. After that your browser caches them.

## Getting it, and keeping it current

```bash
git clone --depth 1 https://github.com/Kepei-Lei102/the-slides-as.git
```

Then, whenever a lesson has run:

```bash
git pull
```

Or just say to your AI assistant: *"the the-slides-as repo updated — pull the new
material and tell me what's new."*

## The other half

The decks teach the lesson; **The Vault** is the reference behind them — a few
hundred cards on Mathematics, Physics and Computer Science, written to be read
rather than presented, and designed for an AI to teach *from*.

```bash
git clone --depth 1 https://github.com/Kepei-Lei102/the-vault-as.git
```

Full setup, including how to point an AI assistant at it: **`SETUP.md`** in this
repo.

---

*Released slides-2026-09-07 · units in this edition: U02a, U02b*
