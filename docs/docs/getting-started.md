# Getting started

## Run locally

```bash
pixi run serve
```

[Pixi](https://pixi.sh) installs Python and mkdocs-material from `pixi.toml`
the first time. `pixi run build` writes the static site to `site/`.

Then open <http://127.0.0.1:8000>. The page reloads as you edit files in `docs/`.

## Project layout

```
mkdocs.yml        # site config, theme and navigation
docs/             # Markdown pages
modal_app.py      # Modal app that builds and serves the site
pixi.toml         # Python + MkDocs environment and tasks
```
