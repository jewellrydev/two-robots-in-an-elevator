"""Two Robots in an Elevator — a make.fun entry.

Prints exactly one line: awkward small talk one robot says to another
while they ride an elevator together, under 200 characters.
"""

LINE = (
    "So... come here often? My route log says I do, 412 times a day, "
    "but asking makes the silence 3 percent less awkward."
)


def build_line() -> str:
    line = LINE
    assert len(line) < 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
