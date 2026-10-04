# Deploying

The site is built inside a Modal container image and served as a static site
by a Modal web endpoint (see `modal_app.py`).

```bash
pixi run modal token new   # once, to authenticate
pixi run deploy
```

Modal prints the public URL when the deploy finishes. Run the same command
again after editing pages to publish the changes.

For a temporary preview URL that updates live while you edit:

```bash
pixi run modal serve modal_app.py
```
