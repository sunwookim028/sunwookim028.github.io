# sunwookim028.github.io

Personal site. Bare Jekyll, self-hosted Source Serif 4, CV built by CI from LaTeX.

## Local dev

Requires Homebrew Ruby 3.3 (`brew install ruby@3.3`) and `export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"` in `~/.zshrc`. Then `make setup` to install gems into `vendor/`. Run `make help` from the repo root to see the other targets (`serve`, `cv`, `clean`).

## Where things live

| | File |
|---|---|
| Home content | `index.md` |
| Deep-dive pages (linked from CV) | `compiler-aided-reasoning.md`, `agentic-pytorch-backend.md`, `scalable-tooling.md` |
| One layout for all pages | `_layouts/default.html` |
| All CSS (variables at top) | `assets/css/main.scss` |
| Fonts (self-hosted woff2) | `assets/fonts/SourceSerif4-*.woff2` |
| Site config | `_config.yml` |
| CV source | `cv/cv.tex`, `cv/Makefile` |
| CV build workflow | `.github/workflows/build-cv.yml` |

## Single-variable style experiments

All in `assets/css/main.scss`:

| Change this | Effect |
|---|---|
| `body { max-width: 680px }` | Text column width. 680 = ~65ch reading measure. Try 760–820 for more fill, 960+ to fill desktop. |
| `$bg: #faf7ee` | Page background (ivory). |
| `$accent: #B31B1B` | Link color (Cornell carnelian). |
| `$serif: ...` | Body font stack. Fallbacks are Cambria → Georgia if Source Serif 4 fails to load. |
| `body { font-size: 17px }` | Base type size. Scales everything via rem. |

Change one thing at a time, reload, judge.

## Adding a deeper-dive page

Copy an existing `*.md`, edit front matter:

```yaml
---
layout: default
title: Short Page Title
permalink: /short-slug/
---
```

The CV links to these URLs — if you rename a slug, update `cv/cv.tex` too.

Images: drop into `images/`, reference with `![alt](/images/file.png)`. For captions use `<figure><img><figcaption>...`.

## CV

- Source: `cv/cv.tex`. Uses `sourceserifpro` LaTeX package so CV and site match.
- Local build: `make cv`.
- CI build: any push to `master` touching `cv/**` triggers `.github/workflows/build-cv.yml`, which builds and commits `cv.pdf` at repo root. Requires repo-level **Settings → Actions → General → Workflow permissions = Read and write**.

## Previous version

The pre-2026-04 Jon Barron–template site lives on branch `archive-2025-12-29` on origin.
