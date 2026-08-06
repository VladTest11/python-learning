# Handoff Document — Python Career Transition

**Purpose:** The single source of truth for this work. Read at the start of every session.
**Last updated:** 6 August 2026

---

## 1. How to use this file

New assistant: read sections 2–5 before responding. Section 6 is the plan; **section 8 is where the last session stopped — start there.** Do not restart the planning conversation — the decisions in section 4 were made deliberately and have reasoning attached. Challenge them if you have evidence, not on general principle.

Work now happens in Claude Code, in the project directory, so code can be run and git driven directly. Demonstrate findings by running them rather than asserting them; it lands better and it catches your own mistakes.

### Picking up next session

1. Read section 8 (session log) for state, then section 3 (working agreement).
2. `git log --oneline` — the history is the record of what was done and why.
3. Resume at the **`grade_calculator.py`** questions in section 8; three questions are outstanding and unanswered.
4. Then `expense_tracker.py` and `bank_accounts.py` (not yet reviewed), then the two remaining M0 items: the **debugger step-through** and the **retrieval check**.

---

## 2. Who I'm working with

- **Name:** Vlad. Based in Serbia. **Relocation to Belgrade or Novi Sad is possible.**
- **Goal:** First paid job as a Python developer. Framed explicitly as a "survive by earning" pivot, not a passion project.
- **Education:** 4-year bachelor's in environmental / sustainable development engineering. Graduated ~2016.
- **Prior work:** Real work experience exists, but employers did not register it with the employment service. **There is no verifiable employment record.** This is the single most important constraint in this document — see section 4.
- **Current Python level:** Can write functions, classes, dictionary and list logic, basic validation. Has completed the exercises in section 5. Has not used: pytest, git, SQL, any web framework, or a debugger.
- **Environment:** macOS, pyenv, Python 3.11.7, VS Code.
- **Availability:** Nominally 3–10 hours/day, but in practice bursty — an intense stretch followed by multi-week gaps when life intervenes. **Plan for interruption, not for speed.** This was learned the hard way; an earlier version of the plan assumed continuous study and was wrong.

---

## 3. Working agreement

These came from stated preferences and from mistakes I made earlier. Please honour them.

- **Ask rather than assume.** Before elaborating, confirm you've understood the task by summarising it. When you notice yourself making a statistical guess about intent, ask instead of building on the guess.
- **Check your own work before presenting it.** Review a solution for inconsistencies and improvements, then present it.
- **Explain the reasoning behind decisions**, not just the decisions.
- **Be concise.** I over-wrote badly in the early sessions — 800-word reviews of 40-line exercises, with the one real bug buried under paragraphs of praise. Lead with the bug. One architectural point. Stop.
- **No numeric scores.** I was scoring exercises 85–99 and the numbers went up regardless of whether Vlad wrote the code or adapted it from online sources. That gives a false read on readiness. Replaced by the two checks in section 6.
- **Method:** requirements → Vlad attempts (time-boxed) → paste code → review → revise. Guided walkthrough only after 20–30 minutes genuinely stuck.

---

## 4. Situation analysis and decisions

### The junior market (researched 6 Aug 2026)

Roughly 70% of companies hiring in 2026 prioritise senior talent; about 12% name juniors as their primary focus. Junior share of hiring reportedly fell from ~15% to ~7%. Roles labelled "junior" frequently ask for 1–3 years.

**Live counts from HelloWorld.rs, the main Serbian IT board (6 Aug 2026):**

| Filter | Ads |
|---|---|
| Python | 60 |
| Java | 26 |
| **Junior seniority, all technologies** | **6** |

Of those six: an infosec analyst (Cisco/IPS), a Junior Data Analyst in Belgrade, a junior software engineer at Logeecom (PHP/C#/JS/SQL, 600–2,000 EUR net), an IT assistant at 60,000 RSD, a 3D modelling AI-trainer role, and a mis-tagged "Senior C++ Engineer".

**Genuine junior software developer roles visible that day: one.** Not Python.

*Caveats:* one board, one day, August (Serbian hiring slows for holidays). Seniority tagging is demonstrably unreliable. Most junior roles never get posted — they go via internships (*prakse*, a separate section on that site), referrals, and company career pages.

### Decisions and reasoning

**Stay on Python.** Vlad chose Python himself in his opening message; it was never examined until now. Examined: it has more than double Java's postings in Serbia. Switching languages costs months and lands in a tier that's equally closed. No reason to switch.

**Three parallel targets, not one.** Aiming solely at "junior Python developer" postings means aiming at a category with roughly one opening at a time. Target simultaneously:
1. Junior backend (Python + SQL + FastAPI/Django)
2. **Internships / prakse** — in this market often the only real door, treated as first-class, not fallback
3. Junior data analyst — appeared in six-of-six on the day, and matches the global pattern of a wider entry door; Python + SQL serves both, so no wasted study

**Backend web over data engineering.** Data engineering postings are ~3% entry-level vs ~8% for data analyst; employers expect production pipeline experience already. It's a second job, not a first.

**Target employer type:** enterprise software vendors, financial institutions, healthcare platforms, infrastructure companies — organisations with long-lived systems still train juniors. Consumer SaaS and startups have cut junior hiring hardest. Belgrade held 84% of openings in the regional data; Novi Sad 11%.

**The environmental engineering background is an asset, not dead weight.** It maps onto utilities, energy, environmental monitoring and sensor data, GIS, and regulatory reporting. A junior with a Python portfolio *and* domain fluency in environmental compliance is a far narrower, less contested candidate than a generic junior. This is the differentiator — build on it deliberately.

**Git history is the substitute for an employment record.** With no registered work history, a timestamped public commit log is the only verifiable evidence of competence Vlad can create unilaterally. This upgrades git from "good habit" to the central artifact of the whole plan. Consistent small commits beat heroic bursts followed by silence — a thin week that still shows commits is worth more than a big week followed by a month of nothing.

**Sweden:** family in Sweden, but the job-seeker permit requires advanced-level (master's-equivalent) education — a 4-year bachelor almost certainly doesn't qualify. UHR credential assessment could confirm. This matters less than it sounds: the main route (employer applies for a work permit after making an offer) has **no degree requirement**, only a salary floor of SEK 33,390/month as of 1 June 2026. So the realistic path is unchanged — become hireable, get an offer, employer sponsors.

**Remote-international is a second job, not a first.** Remote hiring means competing globally, and remote onboarding of a junior is expensive, so those roles skew mid-level and up. When it becomes relevant: the standard Serbian vehicle is registering as a *preduzetnik* on the *paušal* regime (fixed monthly amount, no double-entry books, available under 6,000,000 RSD/year, 50% reduction in year one). Watch the *test samostalnosti* — nine criteria; invoicing one dominant client with fixed hours and their equipment is how people fail it. Talk to an accountant before signing anything.

---

## 5. Work already completed

All in Python, reviewed and revised. Not yet in git, not yet tested with pytest.

1. **`temperature_converter.py`** — functions, validation, exception raising, rounding, docstrings
2. **`string_analyzer.py`** — the dictionary counting pattern (`d[k] = d.get(k, 0) + 1`), `max(d, key=d.get)`, edge cases
3. **`contact_book.py`** — first class; CRUD; `__str__`; `find_by_phone` (caught a real bug: `return None` indented inside the loop, returning on first non-match)
4. **`grade_calculator.py`** — function composition, list comprehensions, accumulator pattern, guard clauses
5. **`expense_tracker.py`** — list-of-dicts design, lambda in `max(key=...)`, generator expression, `if __name__ == "__main__"`
6. **`bank_accounts.py`** — inheritance, `super().__init__()`, method overriding across three subclasses

**Known caveat:** Vlad stated that parts of the ContactBook were adapted from online examples. He can explain the concepts when asked. Treat comprehension as verified, from-scratch production as unverified.

### The paid C# project (recorded 6 Aug 2026)

Vlad has ongoing **paid** work on a private GitHub repo, introduced by a friend. Assessed honestly at his own initiative: the work is **C#, largely AI-model-generated, with Vlad operating the model rather than writing or reading the code.** His words: "I have no real learning value out of it."

**Do not count this as portfolio evidence or as learning time.** A screener who finds it and asks him to walk through the code gets an answer that hurts more than an empty profile. It is also off-stack (C#), so it does not advance M1–M4.

**What it is worth, precisely:** income, and a **character reference** from the friend — showed up, delivered, real client, real codebase. That belongs in M5's references line, not the portfolio. Ask for it; it costs one message.

**Keep the project** — the plan is a survive-by-earning pivot and the income matters. Just file it accurately.

**The pattern to watch:** this is the same failure mode as the ContactBook caveat above, at larger scale — output produced without the ability arriving. It is the reason the two checks in section 6 are the two checks. Neither can be passed by prompting. Vlad diagnosed this himself, unprompted, which is a good sign; reinforce that instinct rather than reassuring him out of it.

**Important:** the gap since the last exercise is **weeks to months, not three weeks** (corrected 6 Aug 2026 — the earlier figure was wrong). Vlad's own read: mechanics likely forgotten, familiarity intact. That distinction matters — the M0 baseline should measure *re-learning speed*, not cold recall, because cold recall after a gap this long is a foregone conclusion and tells us nothing we can act on.

---

## 6. The plan

Milestone-based, not week-based, so a pause doesn't read as failure. No deadlines.

### Two checks replace scoring

1. **Does it pass tests Vlad wrote himself?**
2. **Can he rebuild it from a blank file several days later?**

Only the second measures learning.

### Daily minimum

**30 minutes and one commit.** That's a valid day. A bad week should produce a thinner streak, never a gap. Anything beyond the minimum is a bonus, not the expectation.

### Continuous tracks (run alongside every milestone)

- **Algorithms:** one problem per session, from the start — not a block at the end. Spacing matters more than volume here. Arrays/strings → hash maps → two pointers → recursion → trees.
- **Retrieval:** once per milestone, rebuild one earlier exercise from a blank file, no reference.
- **Reading aloud:** explain one piece of your own code out loud, as if to an interviewer. Interviews test articulation as much as code.

---

### M0 — Infrastructure and honest baseline

*This comes first because it's the evidence layer, and because the gap needs measuring.*

- Install git. One repo, public on GitHub. Commit all six existing exercises.
- **Retrieval baseline:** rebuild `expense_tracker.py` from an empty file, no reference. Expect it to be harder than it feels like it should be. That difficulty is data, not failure.
- Learn `git add / commit / push`, branches, `.gitignore`. Nothing more yet.
- Write a real README for the repo: what it is, how to run it.
- Find and use the VS Code debugger once — set a breakpoint, step through `find_by_phone`.

**Done when:** every exercise is committed, the repo has a README, and you've stepped through code in a debugger.

---

### M1 — Testing and Python consolidation

*Testing moved here from "week 11" in the old plan. It arrives now because it lets Vlad verify his own work instead of waiting for a reviewer.*

- pytest basics: test files, assertions, running the suite.
- **Retrofit tests onto all six existing exercises.** This is the highest-value work in the plan — it re-teaches the old code, catches bugs like the `find_by_phone` one automatically, and makes the repo look professional.
- Exception handling done properly: custom exceptions, when to raise vs return a sentinel.
- File I/O with context managers; JSON and CSV.
- Modules and packages; project structure.

**Exercise — Log Analyzer.** Parse a log file, count levels, find the most common error, list errors with timestamps. *Why:* log parsing is real junior work, and it exercises file I/O plus the counting pattern together.

**Done when:** `pytest` runs green across the repo and you can write a test before writing the function.

---

### M2 — SQL

*Promoted from one line in the old plan to a full milestone. It's heavily tested for junior backend roles and it's also the entry ticket for the data-analyst target — one body of study serving two of the three targets.*

- Relational modelling: tables, keys, relationships.
- `SELECT`, `WHERE`, `JOIN` (inner/left), `GROUP BY`, aggregates, subqueries.
- PostgreSQL locally. `psycopg` or SQLAlchemy from Python.
- Migrations, conceptually.

**Exercise — port the ExpenseTracker to a database.** Same features, PostgreSQL instead of a list. *Why:* it makes the CRUD-to-SQL mapping concrete — `add_expense` becomes INSERT, `get_category_summary` becomes GROUP BY. The pattern he already knows becomes the pattern employers pay for.

**Done when:** you can write a multi-table join with grouping without looking it up.

---

### M3 — First backend API (portfolio project #1)

- HTTP basics: methods, status codes, request/response.
- FastAPI: routes, path and query parameters, Pydantic models, automatic docs.
- REST design; CRUD endpoints against the database from M2.
- Auth basics conceptually; environment variables and secrets.
- Deploy it somewhere free. **A URL a stranger can open is worth more than any amount of local code.**

**Production thinking — do this explicitly.** For every endpoint, write down in the README: what fails, what happens on a timeout, what happens if the same request arrives twice, what gets rolled back. Reports from 2026 interviews consistently say this is what separates candidates — juniors describe the happy path, everyone else describes the failure modes.

**Done when:** it's deployed, tested, documented, and you can walk someone through its failure modes out loud.

---

### M4 — Domain project (portfolio project #2) — the differentiator

**Build something in the environmental / utilities space.** Air quality or water quality data ingestion and dashboard; emissions reporting tool; sensor data pipeline with alerting; regulatory compliance tracker.

*Why this specifically:* it's the only thing in this plan a bootcamp graduate can't replicate. It turns a decade that currently reads as "unrelated" into "domain expert who can also build software." Any Serbian or European company doing utilities, energy, or environmental software should read this project and see someone who already understands their problem space.

Use real open data. Deploy it. Write the README for a hiring manager, not a developer.

---

### M5 — Applications (starts at M3, not at the end)

*Deliberately parallel, not sequential. Applications take weeks to produce responses, and early interviews are diagnostic — they tell you what to study next. Waiting until you feel ready wastes months.*

- CV listing the unregistered work. A CV is not a legal document; list it. Ask those former employers for informal references or LinkedIn recommendations — costs nothing.
- LinkedIn and GitHub as the primary screening surfaces.
- **Channels in priority order:** internships/prakse → referrals and direct outreach → company career pages → job boards. Boards are last because that's where the 800-applicant pools are.
- Target enterprise, fintech, healthcare, infrastructure, and outsourcing firms in Belgrade and Novi Sad. Outsourcing firms are a strong first step: local employment, local hiring bar, international codebase and English exposure — which is what makes a remote or Swedish move possible later.
- Interview practice: explaining code aloud, reading unfamiliar code, and the "what can go wrong" question.

---

## 7. Algorithm problem bank

Source material for the **Algorithms** continuous track in section 6 — one problem per session, from the start. Ordered to match the sequence given there (arrays/strings → hash maps → two pointers → recursion → trees), which supersedes the ordering these came from.

Extracted 6 Aug 2026 from `python_interview_study_plan.md` (the January plan) before deleting it. That file is in git history if anything else is ever wanted from it: `git log --diff-filter=D --oneline -- python_interview_study_plan.md`, then `git show <sha>^:python_interview_study_plan.md`.

**Arrays and strings**
- Two Sum — brute force O(n²) first, then hash map O(n). Do both; the gap between them *is* the lesson.
- Palindrome check — reverse-and-compare, then two pointers. Variations: ignore punctuation, case-insensitive, alphanumeric only.
- Valid parentheses (stack) — `"({[]})"` → True, `"([)]"` → False.
- Reverse a linked list; merge two sorted lists.

**Hash maps** — closest to what's already known, the `d[k] = d.get(k, 0) + 1` pattern from `string_analyzer.py`
- Group anagrams.
- First non-repeating character.
- Sort array by element frequency.
- Min stack with `getMin()` in O(1).

**Two pointers and sliding window**
- Container with most water; three sum; remove duplicates from sorted array.
- Maximum sum subarray of size k; longest substring without repeating characters.
- Fast/slow pointers: linked list cycle detection (Floyd's), middle of a linked list, happy number.

**Recursion**
- Factorial and Fibonacci — write each both recursively and iteratively, and compare.
- Power function `x^n`, done efficiently.
- Generate all permutations of a list.
- Merge sort, then quicksort, both from scratch.

**Trees**
- Implement a binary tree; then the traversals (in/pre/post-order).
- Maximum depth; check if balanced; path sum; lowest common ancestor.

*Note on complexity analysis:* the old plan taught Big-O as a separate topic. Better to pick it up through the paired problems above — Two Sum and palindrome both have a slow and a fast version, and feeling the difference beats memorising notation.

---

## 8. Session log

### 6 August 2026 — first local session (M0)

Moved from the web chat to Claude Code running in the project directory. That changes the method: code can be run, git driven directly, and findings demonstrated rather than asserted. No more copy-paste.

**Done:**

- **Git repo initialised**, `main`, `.gitignore` for Python/macOS. All work committed. Identity set with `git config --local` (not `--global`) deliberately — see the account note below.
- **README written** for the repo.
- **Old January plan deleted.** Its algorithm problems became section 7; the file itself is in git history (`git log --diff-filter=D --oneline -- python_interview_study_plan.md`). Vlad pushed for this — he was right that two plan documents means drift and a permanent tax of remembering which is real.
- **Refresher pass, 3 of 6 files reviewed** (see below).

**GitHub account situation — resolved enough to work, not fully cleaned up:**

- Account is **`VladTest11`**, on `markovicvladimirr@gmail.com`. Also used for the paid C# project, so it has real collaborator access that must not break.
- `vladaah1@gmail.com` **is already registered to some other GitHub account** — likely a forgotten second one. Adding it to `VladTest11` fails with "email is already in use."
- **Decided end state:** rename `VladTest11` → `vladimir-markovic`, with `vladaah1@gmail.com` as primary (it's the inbox he actually reads — Apple ID and devices are on it) and `markovicvladimirr@gmail.com` kept attached as secondary.
- **Deliberately deferred.** The rename needs a checklist first — `@VladTest11` mentions in past issues/PRs don't get rewritten, and `CODEOWNERS`/CI configs referencing the username break silently. Not worth rushing on a live paid project.
- **Commits use `markovicvladimirr@gmail.com`** because it's already verified. Do **not** switch to the GitHub `…@users.noreply.github.com` address — it embeds the username, so a later rename orphans attribution. Plain gmail is rename-proof. With both addresses on one account, either attributes correctly and the mix-ups stop mattering.

### Refresher findings

**Method that worked, keep using it:** Vlad's own idea — comments and docstrings hide whether recall is real, since reading `# key= lets you specify HOW to compare` and feeling recognition isn't remembering. Stripped copies get generated to a scratch dir (script at `strip.py` in the job tmp, easy to rewrite: `ast` for docstring line numbers, `tokenize` for comment columns, rebuild line-by-line — `untokenize` breaks on dropped tokens). Originals never touched. Verify stripped copies produce identical output before use.

- **`temperature_converter.py`** — described it accurately from a skim. Real finding: `float(temp)` also raises `ValueError`, so bad-number and bad-unit failures are indistinguishable to a caller, and the docstring documents only one. Left unfixed for M1.
- **`string_analyzer.py`** — got the return shape and the empty-collection guard (including *why* `max()` errors). Missed `key=`. The gap was not memory: he had not learned that `freq.get` without parentheses is the method passed as a value. Retaught in ~90 seconds with a live demo. Same pattern recurs in `sorted(key=len)` and the lambda in `expense_tracker.py`.
- **`contact_book.py`** — correctly judged `find_by_phone` fixed, and recalled the bug was indentation. Found live: the docstring sat *above* the `def`, making it a discarded expression with `__doc__ = None`. **Vlad fixed it himself mid-session.** Still shaky on `self` — thought it was a call or an initialisation step, not the instance. Retaught as `book.method(x)` → `Class.method(book, x)`. **The M0 debugger task is now targeted: breakpoint in `find_by_phone`, watch `self` in the variables pane and see that it *is* `book`.**
- **`grade_calculator.py`** — **questions asked, not yet answered. Resume here.** Three questions were put to him: (1) predict `process_grades([])` by hand; (2) find where the two validators disagree about reporting bad input — `"Invalid score"` string vs `None`; (3) which of the four statistics values is formatted inconsistently. Question 2 is the one that matters: it's the third file taking a third position on how a function signals failure, and it's the through-line into M1's *raise vs sentinel*. Other findings held back for after he answers: `isinstance(x, (int, float))` accepts `True`/`False` since `bool` subclasses `int`; the `<= 100` halves of the conditions on lines 4 and 31 are already guaranteed by the guard above them; `pass_rate` is unrounded while `average` is rounded.
- **`expense_tracker.py`, `bank_accounts.py`** — not reviewed. Committed as written.

### Read on retention

Better than "unknown" implied. Across three files he was right about return shapes, edge-case guards, a past bug and its cause; the misses were concepts not yet learned rather than facts forgotten — different problem, and re-learning was fast. **The useful metric is re-learning speed, and it is good.** Resist letting him file concept gaps as memory failure; he self-criticises ("I need a brain upgrade") on evidence that doesn't support it.

---

## 9. Open items

- Verify M0 retrieval result — it recalibrates everything after a three-week gap
- Consider UHR credential assessment for the Swedish bachelor question, low priority
- Re-run the HelloWorld junior count outside August; the holiday distortion is real
- Decide the specific M4 domain project once M3 is underway
