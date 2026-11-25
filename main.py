"""One-Line Slogan for a Solana Wallet Agent.

Writes one slogan of at most twenty words, on a single line, to
$MAKEFUN_OUTPUT_DIR/entry.txt: Solana speed with agent brains, a
wallet that reads the market, signs the smart moves, and guards
every lamport. Standard library only.
"""

import os
import sys

WALLET_SLOGAN = (
    "Solana speed, agent brains: your wallet reads the market, "
    "signs the smart moves, and guards every lamport."
)


def slogan_gate(text):
    """Check the slogan against the competition gate.

    The gate wants plain UTF-8 text of at most twenty words, not
    only white space, on a single line: one slogan for a Solana
    wallet agent. Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("slogan must not be only whitespace")
    if len(cleaned.split()) > 20:
        raise ValueError(
            "slogan is %d words, over the 20 word limit"
            % len(cleaned.split())
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("slogan must be exactly one line")
    return cleaned


def slogan_measure(text):
    """Measure the slogan for one last sanity pass.

    Returns a dict with the word count and the character count of
    the cleaned text. A slogan too short to carry an idea, or one
    padded out to fill the cap instead of landing the line, is
    caught here before anything is written.
    """
    words = text.split()
    return {"words": len(words), "chars": len(text)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = slogan_gate(WALLET_SLOGAN)
    shape = slogan_measure(text)
    if shape["words"] < 5:
        raise ValueError("slogan is too short to carry an idea")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
