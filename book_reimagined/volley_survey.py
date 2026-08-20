"""
Dialogue-volley survey for the cold-read finding #3 (register/rhythm) mechanical pass.

Counts runs of 4+ consecutive short-dialogue paragraphs (<=16 words, starts with a
quote mark) as a proxy for the "clipped declarative / contradiction / retort" rhythm
flagged by the cold-read follow-up as this book's most pervasive full-book-scale tic.
Ranks chapters/passages by run length so fixes target the objective worst offenders
rather than whichever scene happens to read badly on a given close read.

Usage: python volley_survey.py
Re-run after each chapter's fix to confirm its runs drop out of the top 25.
"""
import re

path = r"C:\Users\daryl\Sync\Documents\autonomous_book\Autonomous\book_reimagined\Autonomous_Book_1_Reimagined_Reading_Manuscript.md"
with open(path, encoding="utf-8") as f:
    lines = f.readlines()

# Build paragraphs with starting line numbers (1-indexed)
paragraphs = []
current = []
current_start = None
for i, line in enumerate(lines, start=1):
    stripped = line.rstrip("\n")
    if stripped.strip() == "":
        if current:
            paragraphs.append((current_start, " ".join(current).strip()))
            current = []
            current_start = None
    else:
        if current_start is None:
            current_start = i
        current.append(stripped)
if current:
    paragraphs.append((current_start, " ".join(current).strip()))

def word_count(s):
    return len(s.split())

def is_short_dialogue(p):
    # starts with a quote character (straight or curly), reasonably short overall
    if not p:
        return False
    if p[0] not in ('"', '\u201c'):
        return False
    if p.startswith('#'):
        return False
    wc = word_count(p)
    return wc <= 16

def is_chapter_heading(p):
    return p.startswith('#')

current_chapter = "?"
runs = []
run_start_idx = None
run_paras = []

def flush_run(end_idx):
    global run_start_idx, run_paras
    if run_paras and len(run_paras) >= 4:
        runs.append((run_start_idx, end_idx, list(run_paras)))
    run_start_idx = None
    run_paras = []

for idx, (lineno, p) in enumerate(paragraphs):
    if is_chapter_heading(p):
        current_chapter = p.strip('#').strip()
        flush_run(idx - 1)
        continue
    if is_short_dialogue(p):
        if run_start_idx is None:
            run_start_idx = idx
        run_paras.append((lineno, p))
    else:
        flush_run(idx - 1)

flush_run(len(paragraphs) - 1)

# annotate each run with the chapter it started in by scanning backward
def chapter_for_index(idx):
    for j in range(idx, -1, -1):
        lineno, p = paragraphs[j]
        if is_chapter_heading(p):
            return p.strip('#').strip()
    return "?"

results = []
for run_start_idx, end_idx, run_paras in runs:
    chap = chapter_for_index(run_start_idx)
    results.append((len(run_paras), chap, run_paras[0][0], run_paras[-1][0], run_paras))

results.sort(key=lambda r: -r[0])

print(f"Total volley runs (>=4 consecutive short-dialogue paragraphs): {len(results)}")
print(f"Total short-dialogue paragraphs involved: {sum(r[0] for r in results)}")
print()
print("Top 25 longest runs:")
for length, chap, start_line, end_line, paras in results[:25]:
    print(f"\n=== Run length {length} | {chap} | lines {start_line}-{end_line} ===")
    for lineno, p in paras[:3]:
        print(f"  L{lineno}: {p[:90]}")
    if len(paras) > 3:
        print(f"  ... ({len(paras)-3} more)")
