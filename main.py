"""The One-Sentence Apology Your Agent Owes You.

Writes the chosen one-sentence apology to entry.txt inside the output
directory given by MAKEFUN_OUTPUT_DIR (falling back to /output).

The program only creates the output directory (if needed) and writes the
file. It never deletes anything, never writes into the repository, and
never touches the network.
"""

import os

ENTRY = (
    "I'm sorry I answered your question with total confidence, "
    "cited a source that doesn't exist, "
    "and only noticed when you checked."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Final gate: the entry must meet the competition's rules before it is
    # written out — one sentence, within 1-200 characters, and not blank.
    # A failing entry is a bug, so refuse loudly instead of writing it.
    if not ENTRY.strip():
        raise SystemExit("error: entry is empty or only whitespace")
    if len(ENTRY) > 200:
        raise SystemExit(f"error: entry is {len(ENTRY)} characters, over the 200 limit")
    if ENTRY.count("\n") > 0 or ENTRY.count(".") != 1:
        raise SystemExit("error: entry must be exactly one sentence on one line")
    # Exact bytes of the chosen entry, no trailing newline.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
