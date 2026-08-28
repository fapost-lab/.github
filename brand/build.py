#!/usr/bin/env python3
"""Renders one social preview card per repository.

GitHub shows these at 1280x640 wherever a repository link is unfurled — Slack,
X, LinkedIn, a Discord paste. The palette is taken from the organisation's own
logo rather than invented: sampled, it is a near-black #07080d, near-white
#edf0f7, and a gradient running azure #5696fa into violet #5a5ee1.
"""

import base64
import pathlib

HERE = pathlib.Path(__file__).parent
LOGO = base64.b64encode((HERE / "logo.png").read_bytes()).decode()

# repo -> (title, description, the line that says how you get it)
CARDS = {
    "core": (
        "core",
        "Open-source platform for conversational assistants and flow automation",
        "docs.fapost.in",
    ),
    "install": (
        "install",
        "One command to install FaPost Core with Docker Compose",
        'sh -c "$(curl -fsSL https://get.fapost.in/install.sh)"',
    ),
    "foundation": (
        "foundation",
        "Public contracts and DTOs that Solutions and Plugins build against",
        "composer require fapost/foundation",
    ),
    "support": (
        "support",
        "Reusable Eloquent primitives, with no dependency on Core",
        "composer require fapost/support",
    ),
    "website": (
        "website",
        "The site behind fapost.in",
        "fapost.in",
    ),
}

TEMPLATE = """<!doctype html>
<meta charset="utf-8">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  html, body {{ width: 1280px; height: 640px; overflow: hidden; }}

  body {{
    background: #07080d;
    color: #edf0f7;
    font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, sans-serif;
    -webkit-font-smoothing: antialiased;
    position: relative;
  }}

  /* The logo's own gradient, spilled behind it and faded out. Keeps the card
     from reading as a black rectangle with text on it. */
  .glow {{
    position: absolute;
    top: -260px; left: -200px;
    width: 900px; height: 900px;
    background: radial-gradient(circle, rgba(86,150,250,.26) 0%, rgba(90,94,225,.14) 40%, transparent 70%);
  }}

  .frame {{
    position: absolute;
    inset: 72px 88px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  header {{ display: flex; align-items: center; gap: 20px; }}
  header img {{ width: 72px; height: 72px; border-radius: 50%; }}
  header .wordmark {{ font-size: 34px; font-weight: 600; letter-spacing: -.02em; }}
  header .sep {{
    flex: 1; height: 1px;
    background: linear-gradient(90deg, rgba(237,240,247,.16), transparent);
  }}

  h1 {{
    /* inline-block, or background-clip maps the gradient across the full block
       width and the word sits entirely in its first colour. */
    display: inline-block;
    font-size: 96px;
    font-weight: 640;
    letter-spacing: -.035em;
    line-height: 1;
    background: linear-gradient(100deg, #edf0f7 8%, #a8c4fb 46%, #5696fa 78%, #5a5ee1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}

  p {{
    margin-top: 22px;
    font-size: 31px;
    line-height: 1.4;
    color: #9aa0b2;
    max-width: 20ch;
    max-width: 940px;
  }}

  footer {{ display: flex; align-items: center; gap: 18px; }}

  .rule {{ width: 44px; height: 3px; border-radius: 2px;
           background: linear-gradient(90deg, #5696fa, #5a5ee1); }}

  code {{
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    font-size: 27px;
    color: #cfd5e4;
    white-space: nowrap;
  }}
</style>

<div class="glow"></div>
<div class="frame">
  <header>
    <img src="data:image/png;base64,{logo}" alt="">
    <span class="wordmark">FaPost</span>
    <span class="sep"></span>
  </header>

  <div>
    <h1>{title}</h1>
    <p>{description}</p>
  </div>

  <footer>
    <span class="rule"></span>
    <code>{command}</code>
  </footer>
</div>
"""

for name, (title, description, command) in CARDS.items():
    html = TEMPLATE.format(
        logo=LOGO,
        title=title,
        description=description,
        command=command.replace("&", "&amp;").replace("<", "&lt;"),
    )
    (HERE / f"{name}.html").write_text(html)
    print(f"wrote {name}.html")
