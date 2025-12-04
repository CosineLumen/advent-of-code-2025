#!/usr/bin/env python3

INPUT_FILE = "day2-input.txt"


def parse_ranges(line: str) -> list[tuple[int, int]]:
    line = line.strip()
    if not line:
        return []

    ranges: list[tuple[int, int]] = []
    for part in line.split(","):
        part = part.strip()
        if not part:
            continue

        try:
            start_str, end_str = part.split("-", 1)
        except ValueError as exc:
            raise ValueError(f"Invalid range segment {part!r} in line {line!r}") from exc

        try:
            start = int(start_str)
            end = int(end_str)
        except ValueError as exc:
            raise ValueError(f"Invalid integer in range {part!r}") from exc

        if start > end:
            raise ValueError(f"Range start greater than end in segment {part!r}")

        ranges.append((start, end))

    return ranges


def is_repeated_pattern_id(n: int) -> bool:
    """Return True if the number's digits are some pattern repeated at least twice."""
    s = str(n)
    length = len(s)

    # Try all possible pattern lengths up to half the string.
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len != 0:
            continue

        repeat_count = length // pattern_len
        if repeat_count < 2:
            continue

        chunk = s[:pattern_len]
        if chunk * repeat_count == s:
            return True

    return False


def sum_invalid_ids(ranges: list[tuple[int, int]]) -> int:
    total = 0
    for start, end in ranges:
        for value in range(start, end + 1):
            if is_repeated_pattern_id(value):
                total += value
    return total


def main() -> None:
    with open(INPUT_FILE, encoding="utf-8") as f:
        raw = f.read()

    # The puzzle input is a single line, but handle extra whitespace safely.
    parts = [line for line in raw.splitlines() if line.strip()]
    if not parts:
        raise ValueError("Input file is empty")

    # Join in case the line was wrapped, then parse.
    line = "".join(parts)
    ranges = parse_ranges(line)

    result = sum_invalid_ids(ranges)
    print(result)


if __name__ == "__main__":
    main()