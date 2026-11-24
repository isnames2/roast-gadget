# One-Line Roast: The Gadget You Use Every Day
# Entry program: writes one roast line to $MAKEFUN_OUTPUT_DIR/entry.txt.
# Pure Python standard library; deterministic output, no network, no randomness.

import os
from pathlib import Path

# The roast targets a password manager app: it exists to remember passwords,
# yet here it locked its owner out -- the irony is the punchline.
LINE = "My password manager locked me out of my own account, so now I pay a program to forget my password for me."

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
