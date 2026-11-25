# sunwookim028.github.io

Personal homepage. Jekyll on GitHub Pages; layout from [Minimal-Academic-Website](https://github.com/yuhui-zh15/Minimal-Academic-Website), Merriweather to match the CV, accent `#980000`.

| What | File |
|---|---|
| Homepage text | `index.md` |
| Publications | `_data/publications.yml` |
| Page shell (`<head>`) | `_layouts/default.html` |
| Styles | `style.scss` (MIT notice for the template at the top) |
| Photos | `images/` (`sunwoo-2026.jpg` is live) |
| One-off pages | `misc/` (see `misc/README.md`) |

CV is not built here; the site links to the Google Drive copy.

## Preview before pushing

`make preview` serves the site from Docker at http://127.0.0.1:4000 (`PORT=4001 make preview` to change). It rebuilds on save; reload the browser. From a laptop: `ssh -L 4000:127.0.0.1:4000 <server>`, then open http://localhost:4000.

With Ruby 3.3+ on the host instead: `bundle install && bundle exec jekyll serve`.
