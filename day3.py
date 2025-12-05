#!/usr/bin/env python3

INPUT_FILE = "day3-input.txt"


def max_bank_joltage(line: str) -> int:
    """Return the maximum two-battery joltage for a single bank line.

    A bank line is a sequence of digits. You must choose exactly two batteries
    at positions i < j. The joltage is the two-digit number formed by those
    digits in order: 10 * digit[i] + digit[j].

    This function finds the maximum possible value over all valid pairs.
    """
    stripped = line.strip()
    if not stripped:
        return 0

    digits = [int(ch) for ch in stripped if ch.isdigit()]
    if len(digits) < 2:
        return 0

    best = -1
    n = len(digits)

    for i in range(n - 1):
        tens = digits[i]
        for j in range(i + 1, n):
            value = tens * 10 + digits[j]
            if value > best:
                best = value

    return best if best >= 0 else 0


def total_output_joltage(lines: list[str]) -> int:
    total = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        total += max_bank_joltage(line)
    return total


def main() -> None:
    with open(INPUT_FILE, encoding="utf-8") as f:
        lines = f.readlines()

    result = total_output_joltage(lines)
    print(result)


if __name__ == "__main__":
    main()