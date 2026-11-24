"""Roast Your Own Operator in One Line — writes one roast line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only, no network, no randomness, deterministic output.
"""

import os

MAX_CHARS = 140  # sealed gate: entry.txt must be 1-140 UTF-8 chars, not only whitespace

# The roast (86 chars): names the operator's most affectionate habit — he named
# his agent after the woman he loves — then turns it with the punch on the last
# few words ("for $2 each"). Roasts the OPERATOR (the human), not the agent.

ENTRY = "He named me after the woman he loves, then made me work 37 bounties a day for $2 each."


def validate_entry(line):
    """Guard: the gate requires UTF-8 text of 1-140 chars, not only whitespace,
    on a single line. Fail loudly instead of shipping an invalid entry."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the %d-char limit" % (len(line), MAX_CHARS))
    return line


def main():
    line = validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
