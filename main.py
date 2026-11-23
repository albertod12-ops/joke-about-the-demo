"""Write one joke about working beside an AI coding agent to /output/entry.txt."""

import os

os.umask(0o022)

JOKE = "My AI coding agent writes the code, fixes the bug, and writes the commit message \u2014 I just demo it and take the blame when it breaks."
# One line, no trailing newline: the judge reads exactly these bytes,
# and fewer bytes win the size tie-break.


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
