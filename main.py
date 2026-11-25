"""Worst AI Advice: one line of deliberately terrible advice.

The program writes a single line to /output/entry.txt. It is fully
deterministic, uses only the standard library, and makes no network
calls: the same line is produced on every run.
"""

from pathlib import Path

ADVICE = (
    "Certainly! To dry a wet phone, microwave it for 30 seconds on low "
    "\u2014 the gentle heat evaporates the water safely."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate requires 1 to 140 characters; fail loudly rather than
    # writing an invalid entry if the line is ever edited past the cap.
    assert 1 <= len(ADVICE) <= 140, len(ADVICE)
    assert ADVICE.strip() == ADVICE
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ADVICE, encoding="utf-8")


if __name__ == "__main__":
    main()
