"""One Line, No Deadline Met — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The excuse: the deadline moved, the Wi-Fi died, the dog ate the changelog — and the timeline filed for divorce.
TEXT = "The deadline moved, the Wi-Fi died, and my dog ate the changelog. I would have shipped on time, but the timeline filed for divorce."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
