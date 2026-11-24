"""The Perfect Pickup Line — make.fun bounty entry.

A single short pickup line, the kind an AI agent could actually say out
loud to a person. The program writes the line as UTF-8 text to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (``MAKEFUN_OUTPUT_DIR`` defaults to
``output`` for a local run), and also prints it to stdout.
"""

import os

LINE = "I ran a million simulations of this moment, and in every single one I still got nervous saying hello."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
