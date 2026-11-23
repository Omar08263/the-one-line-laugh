"""The One-Line Laugh — entry program (program/v1, Python 3.13, stdlib only).

Writes one original funny line (a single sentence, <= 200 characters) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set, for local runs).
Deterministic: the same bytes on every run; no network, no randomness,
no reads outside this file.
"""

import os

LINE = "My phone's been on 1% for forty minutes now, and I've decided it's not dying \u2014 it's just dramatic."

# Gate the line itself: one sentence, 1-200 characters, not only whitespace.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
assert LINE.strip(), "line must not be only whitespace"
assert LINE.count(".") == 1 and LINE.endswith("."), "line must be a single sentence"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # Read-back check (thinking_revised): the file on disk must hold exactly
    # the approved line, byte for byte; otherwise fail loudly, never silently.
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt does not match the approved line")


if __name__ == "__main__":
    main()
