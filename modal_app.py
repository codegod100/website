"""Build the MkDocs site into a Modal image and serve it as static files."""

from pathlib import Path

import modal

HERE = Path(__file__).parent
SITE_DIR = "/site"

image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("mkdocs-material>=9.5", "fastapi[standard]")
    .add_local_file(HERE / "mkdocs.yml", "/src/mkdocs.yml", copy=True)
    .add_local_dir(HERE / "docs", "/src/docs", copy=True)
    .run_commands(f"cd /src && mkdocs build --strict --site-dir {SITE_DIR}")
)

app = modal.App("mkdocs-website", image=image)


@app.function()
@modal.concurrent(max_inputs=100)
@modal.asgi_app()
def web():
    from fastapi import FastAPI
    from fastapi.staticfiles import StaticFiles

    api = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
    api.mount("/", StaticFiles(directory=SITE_DIR, html=True), name="site")
    return api
