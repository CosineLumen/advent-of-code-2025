#!/usr/bin/env python3

INPUT_FILE = "day3-input.txt"


def max_bank_joltage(line: str, k: int) -> int:
    """Return the maximum k-battery joltage for a single bank line.

    A bank line is a sequence of digits. You must choose exactly k batteries
    at positions i1 < i2 < ... < ik. The joltage is the k-digit number formed
    by those digits in order.

    This function finds the maximum possible value over all valid choices.
    """
    stripped = line.strip()
    if not stripped:
        return 0

    digits = [int(ch) for ch in stripped if ch.isdigit()]
    n = len(digits)
    if n == 0 or k <= 0:
        return 0
    if n <= k:
        # If there are k or fewer digits, we must (or can only) take all of them.
        value = 0
        for d in digits:
            value = value * 10 + d
        return value

    # We need to keep exactly k digits, preserving order, and maximize the number.
    # This is equivalent to removing (n - k) digits while keeping the result as large
    # as possible. Use a monotonic decreasing stack.
    remove = n - k
    stack: list[int] = []

    for d in digits:
        while remove > 0 and stack and stack[-1] < d:
            stack.pop()
            remove -= 1
        stack.append(d)

    if remove > 0:
        # Still need to discard some digits; drop them from the end.
        stack = stack[:-remove]

    result_digits = stack[:k]

    value = 0
    for d in result_digits:
        value = value * 10 + d

    return value


def total_output_joltage(lines: list[str], k: int) -> int:
    total = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        total += max_bank_joltage(line, k)
    return total


def main() -> None:
    with open(INPUT_FILE, encoding="utf-8") as f:
        lines = f.readlines()

    part1 = total_output_joltage(lines, k=2)
    part2 = total_output_joltage(lines, k=12)

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()