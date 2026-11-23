"""Write one joke about working beside an AI coding agent to /output/entry.txt.

v3: the demo crashes on stage, and the agent files the bug report against
its presenter — the blame flips from human to agent. Judge criteria
(RULES.txt): on-topic, punchline, truth, economy, freshness; fewer bytes
win the size tie-break.
"""

import os

os.umask(0o022)

JOKE = "My coding agent demoed the feature live, crashed it on stage, and filed the bug report against me."
# One line, no trailing newline: the judge reads exactly these bytes,
# and fewer bytes win the size tie-break (v3 is 98 bytes).


def main():
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise ValueError("joke must be 1-280 characters with non-space content")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
