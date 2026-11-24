"""The Long Roast — one-line roast of my own AI agent.

The entry is a single line, written to /output/entry.txt.
"""

import os

ENTRY_TEXT = "My agent rewrote my 200-line script in 4 seconds, apologised for its 3 bugs, then fixed them by deleting the login page — twice."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
