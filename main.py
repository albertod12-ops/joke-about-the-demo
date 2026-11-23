"""One-line joke about demo day with an AI coding agent.

Writes exactly one line to /output/entry.txt: the joke bytes and nothing
else. No trailing newline is added, so the file size equals the joke
length (98 bytes). The output file is left world-readable; the /output
directory itself is never touched beyond creating it if missing.
"""

import os

JOKE = "My coding agent demoed the feature live, crashed it on stage, and filed the bug report against me."

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280


def write_joke():
    text = JOKE
    if not text.strip():
        raise ValueError("joke is empty")
    if len(text) > MAX_CHARS:
        raise ValueError("joke exceeds 280 characters")
    os.umask(0o022)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    write_joke()
