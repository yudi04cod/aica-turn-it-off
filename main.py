#!/usr/bin/env python3
"""Have You Tried Turning It Off? -- make.fun entry.

Writes one funny line from a hopeless tech support agent to a desperate
customer to /output/entry.txt. Python standard library only, deterministic,
no network, no randomness.
"""

import os

# The twist on the classic: the agent does not fix anything either -- he
# admits the computer is copying his own Monday-morning helplessness, then
# cheerfully proposes the one move he knows (restart it together). The
# customer is never mocked; the agent's uselessness is the joke.
LINE = (
    "Good news \u2014 your computer isn't broken, it's just doing what I do "
    "every Monday: staring at the screen and hoping someone else fixes it. "
    "Let's restart it together."
)


def main():
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    text = LINE.strip()
    if not (1 <= len(text) <= 199):
        raise SystemExit("entry must be 1-199 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise SystemExit("entry must not contain control characters")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(out_path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        raise SystemExit("read-back mismatch")
    print("wrote %d characters to %s" % (len(text), out_path))


if __name__ == "__main__":
    main()
