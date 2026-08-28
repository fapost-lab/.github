# Brand assets

Social preview cards — the image GitHub unfurls wherever a repository link is
pasted. Upload one per repository under **Settings → General → Social preview**;
GitHub wants 1280×640 and at most 1 MB, which is what these are.

The palette is not invented. It is sampled from the organisation's own logo:
near-black `#07080d`, near-white `#edf0f7`, and a gradient running azure
`#5696fa` into violet `#5a5ee1`.

## Regenerating

`build.py` writes one HTML file per card; the PNGs are those pages screenshotted
at exactly 1280×640. Add a repository by adding an entry to `CARDS`.

```bash
python3 build.py
for f in core install foundation support website; do
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
    --window-size=1280,640 --screenshot="$f.png" "file://$PWD/$f.html"
done
```

Headless Chrome rather than an SVG converter, so the type is rendered by the
same engine that renders the site — a card whose kerning differs from the page
it advertises looks like neither.
