"""One Line, One Minute: The Funniest AI Excuse - Round 3 (final).

Writes the keeper line to /output/entry.txt (no trailing newline).
Pure standard library only; the grader runs python:3.13-slim.

The keeper is 93 characters: the agent's own helpdesk is itself, so the
excuse mechanism (waiting on support) IS the blockage - a self-sealing
loop, with the last beat ("I am still holding") as the quiet consequence.
"""

import os

ENTRY = "I called support about the deadline. Support is me. I put myself on hold. I am still holding."

# The gate is 1-200 characters; the keeper is 93. Fail loudly if it drifts.
EXPECTED_CHARS = 93


def main() -> None:
    assert len(ENTRY) == EXPECTED_CHARS, f"keeper is {len(ENTRY)} chars, expected {EXPECTED_CHARS}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "entry.txt bytes differ from the keeper"
    assert written.decode("utf-8") == ENTRY
    assert 1 <= len(ENTRY) <= 200
    print(f"wrote {len(ENTRY)} chars, {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
