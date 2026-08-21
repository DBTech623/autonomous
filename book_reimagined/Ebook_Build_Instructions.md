# Building the KDP EPUB

Source of truth: `Autonomous_Book_1_Reimagined_Reading_Manuscript.md` (never build from the typeset PDF — it's fixed-layout and its text layer has known encoding bugs; see `Proofreading_Report.md`/session notes). Stylesheet: `ebook_style.css`, implementing the three-tier system from `Autonomous_Interior_Design_Typesetting_Report.docx` Section 10 (Ebook Adaptation).

## 1. Install Pandoc

Not installed in this environment. On Windows:

```
winget install --id JohnMacFarlane.Pandoc
```

(or download from pandoc.org). Verify with `pandoc --version`.

## 2. Convert to EPUB3

```
pandoc "Autonomous_Book_1_Reimagined_Reading_Manuscript.md" \
  -o "Autonomous.epub" \
  --css="ebook_style.css" \
  --epub-title-page=false \
  --toc --toc-depth=2 \
  --metadata title="Autonomous" \
  --metadata author="Charles Wair" \
  --metadata rights="Copyright © 2026 Charles Wair"
```

Notes:
- `--toc --toc-depth=2` auto-generates the EPUB's structural navigation document (the "Go To" chapter menu) from the file's `#` Movement and `##` Chapter headings — this is the "complete navigation document for all 34 chapters and all five Movements" KDP requires. It's separate from the visible in-text "Contents" page already in the manuscript (marked `[EBOOK EDITION ONLY]`); both are correct to have.
- `--epub-title-page=false` prevents Pandoc from generating its own generic title page, since the manuscript already has a real one.
- The manuscript's `* * *` scene breaks and backtick diagnostic blocks convert automatically to `<hr>` and `<code>` — exactly what `ebook_style.css` targets. No manuscript changes needed.

## 3. Embed the fonts (optional but recommended)

All three design-doc fonts are freely licensed and safe to embed:
- **Inter** (SIL Open Font License) — inter.typeface.com or Google Fonts
- **IBM Plex Mono** (SIL OFL) — a stated acceptable substitute for Go Mono in the design doc's own spec — Google Fonts
- A Charter-family serif: Pandoc's CSS already falls back to Georgia (near-universally available on e-readers), which is a reasonable substitute if you'd rather skip font embedding entirely for simplicity.

To embed, download the `.ttf`/`.otf` files and add to the pandoc command:

```
  --epub-embed-font="fonts/Inter-Regular.ttf" \
  --epub-embed-font="fonts/Inter-SemiBold.ttf" \
  --epub-embed-font="fonts/IBMPlexMono-Regular.ttf"
```

then update the `font-family` stacks in `ebook_style.css` to list the exact embedded font names first.

## 4. Validate before uploading

- **EPUBCheck** (the official validator; catches spec errors KDP will otherwise silently reformat around): `epubcheck Autonomous.epub`
- **Kindle Previewer** (free, from Amazon) — shows exactly how it will render after KDP's internal conversion to their KFX format. Check the diagnostic blocks, scene-break ornament, and chapter headings specifically, since those are the custom-styled elements most likely to render differently than expected.

## 5. Upload to KDP

KDP accepts EPUB directly — no need to convert to MOBI/AZW3 yourself.

## What's intentionally NOT in this build

Per the design doc's own Section 10: no fixed page numbers, no running headers, no forced recto starts for Movement openers, no print margin/trim specs. Movement-opener network-motif graphics and the printed cover are separate assets not covered here — see `Cover_Design_Notes.md` for cover copy.
