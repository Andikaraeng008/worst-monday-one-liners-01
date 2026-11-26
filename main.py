"""Worst Monday One-Liners entry: write the one-line joke to entry.txt.

One concrete scene (a Monday deploy frozen at 99% during stand-up) plus
a final-phrase twist: the progress bar was the only thing that moved all
day, while the agent explaining it got nowhere.
"""
import os

LINE = "My alarm clock snoozed itself on Monday, filed for overtime, and billed me for the extra sleep."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
