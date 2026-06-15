# CLAUDE.md — Zhaoyang Chu's Academic Homepage

Inherits the global workflow in `~/.claude/CLAUDE.md` (Git-as-universal-workflow, branch → PR → merge,
tag conventions). This file adds repo-specific context so any future session can edit without re-asking.

## What this repo is

My personal academic homepage, served at **https://zhaoyang-chu.github.io** via GitHub Pages.
Built on the **AcadHomepage** Jekyll template (RayeRen/acad-homepage.github.io). It is a long-lived
platform for my academic brand: I update papers, news, and bio here regularly.

The whole site is effectively a **single page** — almost all content lives in one file.

## Where things live

| Path | What it is | Touch frequency |
|------|------------|-----------------|
| `_pages/about.md` | **The only content page** — the homepage. News, Publications, Honors, Educations all live here. | ⭐ Primary |
| `_config.yml` | Site config: title, avatar, location, social links (Google Scholar, GitHub, LinkedIn, ORCID, Twitter, email). | Occasional |
| `_data/navigation.yml` | Top nav-bar anchors. Add an entry when adding a new top-level `#` section to about.md. | When adding sections |
| `images/` | Per-paper thumbnails + `profile.jpg` avatar. | When adding a paper |
| `assets/` | `ZhaoyangChu_CV.pdf`, paper PDFs, css/js/fonts. | When updating CV |
| `_includes/`, `_layouts/`, `_sass/` | Template HTML + styles. Rarely touched. | Almost never |
| `google_scholar_crawler/` + `.github/workflows/google_scholar_crawler.yaml` | Auto-updates citation counts. | Fully automated — don't touch |

## Identity (keep consistent everywhere)

- First-year PhD student, Dept. of Computer Science, **UCL**. Co-supervised by Prof. Federica Sarro and Dr. He Ye.
- MSc from **HUST** (advisor Prof. Yao Wan); collaborations with Prof. Lingming Zhang (UIUC) and Prof. Hongyu Zhang (Chongqing Univ.).
- Research: intersection of SE and AI — **reliable and safe coding agents** for real-world SE workflows.
- Primary email: **zhaoyang.chu.25@ucl.ac.uk** (also zychu418@gmail.com). This is the email in `_config.yml` and about.md — keep them in sync.

## Most frequent task: adding a publication

1. Drop the thumbnail into `images/` (jpg/png; rendered at `width="100%"` inside the box).
2. In `_pages/about.md`, copy an existing `<div class='paper-box'>` block into the Publications section.
   Publications are ordered **Preprints first, then by venue/recency** (newest/most prestigious near the top).
3. The block template:

```html
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">VENUE or "Preprint"</div><img src='images/THUMB.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Paper Title**.<br>
Author A, [**Zhaoyang Chu**](https://zhaoyang-chu.github.io/), Author C†.<br>
[**VENUE YEAR**](venue-url). *Full venue name*.<br>
\[ [Paper](url) \] \[ [Code](url) \] \[ [Homepage](url) \] \[ [Dataset](url) \]

</div>
</div>
```

   - My name is always bolded and linked: `[**Zhaoyang Chu**](https://zhaoyang-chu.github.io/)`.
   - `\*` after a name = equal contribution; `†` = corresponding author. There's a legend line near the top of Publications.
   - Only include link brackets that exist (Paper / Code / Homepage / Dataset).
   - **Citation count:** append `<span class='show_paper_citations' data='HYu3DyEAAAAJ:PUB_ID'></span>` after the last link bracket so the paper shows `| Citations: N`. Find `PUB_ID` (the `author_pub_id`) in `gs_data.json` on the `google-scholar-stats` branch — match by title. New papers not yet indexed by Google Scholar have no `PUB_ID`; skip the span for those (a span with a bad id throws a JS error that breaks **all** per-paper counts). The total-citations shields badge near the top updates automatically and needs no per-paper edit.
   - **GitHub stars / HuggingFace downloads badges** (live shields.io, appended after the citation span on the same line):
     - Stars (one per GitHub repo): `![GitHub stars](https://img.shields.io/github/stars/OWNER/REPO?style=flat-square&logo=github&label=stars)`
     - HF downloads (one per HF dataset, shows **all-time** downloads): `![HF downloads](https://img.shields.io/badge/dynamic/json?style=flat-square&url=ENCODED_HF_API_URL&query=%24.downloadsAllTime&label=%F0%9F%A4%97%20downloads&color=ff9d00)` where `ENCODED_HF_API_URL` is `https://huggingface.co/api/datasets/OWNER/NAME?expand=downloadsAllTime` percent-encoded. Use `expand=downloadsAllTime` (the plain `downloads` field is only the last 30 days; `downloadsAllTime` requires the `expand`). Note: use `expand=...`, **not** `expand[]=...` — shields rejects the bracketed form with `invalid query parameter: url`.
4. Add a matching News line at the top of the `# 🔥 News` list:
   `- *YYYY.MM*: &nbsp;🎉 Our work on *topic* was accepted to **VENUE**.`
5. If it's an award or new section, also update `# 🎖 Honors and Awards` / `_data/navigation.yml`.

## Conventions

- **Dates** use `*YYYY.MM*` format in News and Educations.
- Commented-out `<!-- ... -->` paper-box / news blocks are intentionally parked (old preprints, hidden papers) — leave them unless asked.
- Don't hand-edit citation counts; the GitHub Action regenerates them on the `google-scholar-stats` branch weekly (Mon 08:00 UTC), on any Pages build, or via manual `workflow_dispatch`. Note: `scholarly` scrapes from a shared GitHub Actions IP that Google Scholar rate-limits, so individual runs fail intermittently — a missed week is normal and self-heals on the next successful run; the failed run won't overwrite good data (the step exits before pushing).

## Running locally

```bash
./run_server.sh   # bundle exec jekyll liveserve
```

Environment requirements (set up once; macOS system Ruby 2.6 will **not** work):
- **Ruby 3.3.x via rbenv** — pinned in `.ruby-version` (3.3.11), matching GitHub Pages' own Ruby. Installed with `brew install rbenv ruby-build && rbenv install 3.3.11`. `rbenv init` is in `~/.zshrc`.
- **UTF-8 locale** — `export LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8` (in `~/.zshrc`). Without it the sass build dies with `Invalid US-ASCII character` on non-ASCII chars in the styles.
- `Gemfile.lock` was re-resolved (`bundle update`) off the original Ruby-2.6-era pins to versions compatible with Ruby 3.3. GitHub Pages ignores `Gemfile.lock` and builds with its own bundle, so this only affects local dev.

## Git workflow for this repo

Per global rules: branch → PR → merge even for solo edits; keep `main` clean.
Tag milestones, e.g. `release/<event>` when refreshing for a conference or job-market push.
