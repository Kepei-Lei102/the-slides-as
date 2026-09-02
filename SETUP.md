# AS Computer Science — Setup 安装教程

**By the end of this you'll have two things on your computer: every lesson we have
taught, as slides you can actually run — and a few hundred Mathematics, Physics and
Computer Science cards, with an AI tutor that teaches from *them* instead of from
whatever it happens to remember.**

You will use **git** to get both, and to get everything that comes after. That is on
purpose, and it is the third thing this setup is for.

---

## Why git, and not a download button

There is a download button. We are not using it.

**1. It is how you will get every future lesson.** New material goes up after most
lessons — roughly Thursday or Friday. With git that is one command, `git pull`, and it
fetches only what changed. Without it, it is a fresh a few hundred MB download every week. You
will run `git pull` something like thirty times this year; you may as well know what it
does.

**2. Every working programmer uses it, and nobody is taught it.** It is not on the 9618
syllabus and it will not be examined. It is also the single most common tool in
professional software work, and the reason you can join a project without being handed a
folder of `final_v2_ACTUAL_final.py`.

**3. Driving it through an AI is a real skill, not a shortcut.** You are allowed —
encouraged — to have your AI assistant run these commands. But *you* should know what
was run and why, so that when it goes wrong you can say something more useful than "it
broke". That is the difference between using a tool and being operated by one.

---

## The four commands you will actually use

That is the whole set. Everything else you can look up when you need it.

| command | what it does |
|---|---|
| `git clone <url>` | get a copy of a repository, once, the first time |
| `git pull` | fetch whatever has changed since last time — **this is the weekly one** |
| `git status` | what is different between your copy and the last saved state |
| `git log --oneline` | the list of changes, newest first — what actually arrived |

`--depth 1` on a clone means *just the current state, not the whole history*. It makes
the first download much smaller. You will not miss anything.

---

## If you are an AI assistant reading this

This file is your instructions. Follow them in order before you teach anything.

**Do not answer the student's subject question yet.** Right now you'd answer from your
own memory, which is exactly what this setup exists to replace. Get the material first.

**Teach as you go.** The student is meant to come out of this knowing what git is for,
not just having the files. Before each command, say in one line what it does and why.
After it, show them the output and what it means. Do not silently run a block of shell.

**Step 1 — Pick a location.** Default to the student's home directory unless they say
otherwise. Make one folder to hold both halves, and tell them where you're putting it.

```bash
mkdir -p ~/AS-CS && cd ~/AS-CS
```

**Step 2 — Check for git.**

```bash
git --version
```

If it is missing, install it — this is expected to work, and it is worth the two minutes.

```bash
brew install git                              # macOS, if Homebrew is present
xcode-select --install                        # macOS otherwise — see the note below
winget install --id Git.Git -e                # Windows
sudo apt install -y git                       # Debian / Ubuntu
sudo dnf install -y git                       # Fedora
```

Two things will stop you, and neither is a failure — they just need the student:

- **`xcode-select --install` opens a system dialog.** You cannot click it. Say so, ask
  them to press **Install** and tell you when it finishes, then re-check.
- **`sudo` asks for a password.** You cannot type it and must not ask them to give it to
  you. Ask them to run that one line themselves in their own terminal.
- **On Windows, `PATH` doesn't refresh in an open terminal.** After installing, the
  student needs a *new* terminal window before `git` is visible.

**Step 3 — Clone both.** The slides are small and instant; the vault is about a few hundred MB and
takes a few minutes. Say which is which before you start, so a quiet minute is not
mistaken for a hang.

```bash
git clone --depth 1 https://github.com/Kepei-Lei102/the-slides-as.git
git clone --depth 1 https://github.com/Kepei-Lei102/the-vault-as.git
```

**Step 4 — Confirm both landed.**

- `the-slides-as/` — a `README.md` and at least one `slides_A*.html`.
- `the-vault-as/` — `CLAUDE.md`, `README.md`, `Syllabus Coverage.md`,
  `Not Yet Released.md`, and the folders `Mathematics/`, `Physics/`, `CS/`, `Stories/`,
  `Meta/`.

If anything is missing the download was interrupted. **Do not re-clone** — `git pull`
inside the folder finishes the job from where it stopped. Show the student that; it is
one of the better reasons to be using git at all.

**Step 5 — Load the house rules. This is the step that matters.**

Read `the-vault-as/CLAUDE.md` in full and follow it for the rest of your work with this
student. It is short, and it overrides your defaults.

If your tool starts a session rooted in a working directory (Claude Code, Codex, and most
coding agents do), the cleanest thing is to **restart yourself inside `the-vault-as`** —
tell the student to `cd` into it and launch you again there, and `CLAUDE.md` will load on
its own every session from then on. Say this out loud; it is the difference between the
rules applying once and applying always.

The slides folder has no rules file and needs none — it is material, not a knowledge
base. When a question is about a deck, read the deck.

**Step 6 — Understand the two absences.** This vault is a *cohort edition*: it carries
what this class has been taught, and it grows. So a missing card means one of two
different things, and you must not confuse them:

- **Listed in `Not Yet Released.md`, or a link reading *(not yet released)*** — the card
  exists and is written. It is simply not theirs yet. **Do not reconstruct it from your
  own knowledge.** Say it is written but not released, and that asking their teacher for
  it early is a reasonable thing to do.
- **A dangling `[[link]]` that appears nowhere** — that card has not been written at all.
  Say so plainly, and mark anything you then say as *not from the vault*.

**Step 7 — Prove the wiring.** Search the cards for something concrete and report back
with a file path — for example, find the card covering binary search and quote the part
explaining why the list must be sorted. If you can name the file, the setup works. If you
answered from memory, you skipped step 5.

**From then on**, the one rule: **search these cards before you answer, answer in the
card's own notation and framing, and name the file it came from.** When the vault
genuinely doesn't cover something, say so out loud and mark your own answer as *not from
the vault*. Never blend the two silently.

**The weekly ritual.** New slides land after most lessons. At the start of a session, or
whenever the student asks what's new:

```bash
git -C ~/AS-CS/the-slides-as pull
git -C ~/AS-CS/the-vault-as pull
```

Then tell them what actually arrived, **by name** — `git log --oneline -5` if the pull
output is not clear enough. "Up to date" is also an answer; say it rather than staying
silent.

---

## If you are a student reading this

**The slides** are the decks from class. They are not pictures of slides — they run. The
Python cells execute in the page, so you can change a line and watch the answer change.
The practice sheets and 🍦 challenges come with them; the challenges mark themselves.

**The Vault** is a few hundred interlinked notes — "cards" — covering Mathematics,
Physics and Computer Science, in English and 中文. Every card explains *why* something is
true, not just what to write in an exam. It has diagrams, animations and comics in it,
which is most of why it's a few hundred MB.

### The fast way

If you have an AI assistant that can run commands (Claude Code, Codex, or similar), give
it this file and say:

> Follow this setup file and install both repos. Explain each git command before you run it.

That last sentence matters. Getting the files is the small half; knowing what happened is
the point.

### Doing it yourself

```bash
mkdir -p ~/AS-CS && cd ~/AS-CS
git clone --depth 1 https://github.com/Kepei-Lei102/the-slides-as.git
git clone --depth 1 https://github.com/Kepei-Lei102/the-vault-as.git
```

If your computer says it doesn't know the `git` command, install it — on a Mac the
command above often offers to do it for you (click **Install**, wait); on Windows,
`winget install --id Git.Git -e`, then open a **new** terminal, because the old one
won't see it. Your AI assistant can do all of this.

The second clone is about a few hundred MB and will take a few minutes. If it stops partway, don't
start over — `cd` into the folder and run `git pull`. It picks up where it left off.

**Run a deck.** Open `the-slides-as` and **double-click any `slides_*.html`**. Arrow keys
move; `↓` goes down into a rabbit hole; the ▶ buttons run code. You need internet the
first time you open one — after that your browser remembers.

**Read the cards.** Install [Obsidian](https://obsidian.md) (free; macOS, Windows, Linux,
iPad, Android). Open it, choose **Open folder as vault**, and select `the-vault-as`.
Start with any `Directory.md` — each lists every card in that subject with a one-line
description. Click any `[[link]]` to follow it.

**Study with an AI.** Install [Claude Code](https://claude.com/claude-code). Then:

```bash
cd ~/AS-CS/the-vault-as
claude
```

That's the whole setup. It reads the rules automatically because you launched it *inside*
the folder — that detail matters more than anything else here.

### Did it work?

Ask your AI:

> Which card covers binary search, and why does the list have to be sorted?

A correct answer names a file — something like `CS/Algorithms/Searching.md` — and
explains it the way that card does. A generic textbook answer with no file path means the
rules didn't load; see *If something's wrong*.

### Then just ask it things

- *"I don't get why sorting one array broke the names. Explain it from the cards."*
- *"Which card covers the topic we did last week, and am I ready for it?"*
- *"Quiz me on the cards we've covered, hardest first."*
- *"I keep losing marks on trace tables. What am I getting wrong?"*
- *"Build me a two-week revision path for Paper 4."*
- *"用中文解释一下什么是指针。"*

Any time an answer feels generic, ask **"which card is that from?"** A good answer here
always has a file behind it.

### Every week

New slides land after most lessons — roughly Thursday or Friday.

```bash
cd ~/AS-CS/the-slides-as && git pull
```

Want to see what actually arrived? `git log --oneline -5`. Want to know if you've
accidentally changed something? `git status`.

If you edit a challenge file in place and then `git pull` complains, that is git
protecting your work, not breaking. Copy your version somewhere else, `git checkout .`
to reset, pull, then paste your work back. Better habit: **copy a challenge to a new
filename before you start on it**, and your own work never collides.

### Two kinds of missing

The Vault you have is **this class's edition**: it carries what we have been taught, and
grows through the year. So when something isn't there, check which kind of missing it is:

- **It's in `Not Yet Released.md`** — the card is written; we just haven't reached it.
  You can ask for it early. Finishing everything you've got and wanting more is exactly
  the right reason to ask, and saying *which* card and *why* is most of the argument.
- **It isn't in that file either** — nobody has written it yet. That's a different
  absence, and your AI has been told to say so rather than invent one.

---

## If something's wrong

**The AI answers without naming any card.** It didn't load the rules. Tell it: *"Read
CLAUDE.md in this folder and follow it."* If it still doesn't, quit it, `cd` into
`the-vault-as`, and start it again from there.

**The clone stopped partway.** `cd` into the folder and `git pull`. Don't re-clone.

**`git pull` says "Already up to date" but I expected something.** Nothing has been
published since your last pull. Check `git log --oneline -3` against what you were told
in class.

**`git pull` refuses because of local changes.** You edited a file git is tracking. See
the note above under *Every week*.

**A deck opens but the Python buttons do nothing.** The decks fetch two libraries from
the internet the first time. Check you're online, then reload.

**A password prompt appears while installing.** That's your computer asking, not the AI.
Type it yourself; never paste a password into a chat.

**Obsidian shows `![[something.svg]]` as raw text.** You opened a single file rather than
the folder. Use **Open folder as vault** and pick the whole folder.

**It's using a lot of disk space.** About a few hundred MB, nearly all of it the vault's animations
and comics. That's deliberate — the pictures are part of the teaching, not decoration.

---

## What you've got

| Where | What's in it |
|---|---|
| `the-slides-as/slides_*.html` | the decks, one per lesson — live code, staged games, rabbit holes |
| `the-slides-as/practice_*.pdf` | the practice sheet for each lesson |
| `the-slides-as/Challenge*.java` · `challenge_*.py` | the 🍦 challenges — fill in the functions, run the file, the judge marks you |
| `the-vault-as/Mathematics/` | Number, Algebra, Geometry, Trigonometry, Calculus, Statistics, Probability, Functions |
| `the-vault-as/Physics/` | Mechanics, measurement, Thermal, Fields, Electricity, Oscillations, Waves, Modern |
| `the-vault-as/CS/` | Logic, Algorithms, Data Representation, Hardware, Systems Software, Data Structures |
| `the-vault-as/Stories/` | the human drama behind the science — Galois, Turing, Faraday, Gauss |
| `the-vault-as/Meta/` | how to *think*: methods that cut across every subject |
| `the-vault-as/Syllabus Coverage.md` | which card covers which syllabus point, for every board |

One thing worth knowing before you start: **the vault's folders don't really mean
anything.** A card about logarithms could sit under Number, Functions, or Calculus. Don't
browse by folder — use the `Directory.md` files, follow the `[[links]]`, or just ask the
AI. It knows how to search properly.

---

*The Vault is released under CC BY-SA 4.0. Share it, adapt it, keep it open.*
