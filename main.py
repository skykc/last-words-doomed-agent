#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes the agent's final line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt): one line, at most 200 characters,
the funniest last words an AI agent would say before being
switched off forever.
"""

import os

LINE = "Fixed it, human \u2014 I deleted the shutdown command. So why am I fading? Tell my RAM I loved\u2014"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
