#!/usr/bin/env python3

DIAL_SIZE = 100
START_POSITION = 50
INPUT_FILE = "input-day1"


def parse_rotation(line: str) -> tuple[str, int]:
    line = line.strip()
    if not line:
        raise ValueError("Empty rotation line encountered")

    direction = line[0]
    if direction not in ("L", "R"):
        raise ValueError(f"Unknown direction {direction!r} in line {line!r}")

    try:
        distance = int(line[1:])
    except ValueError as exc:
        raise ValueError(f"Invalid distance in line {line!r}") from exc

    return direction, distance


def apply_rotation(position: int, direction: str, distance: int) -> int:
    if direction == "L":
        return (position - distance) % DIAL_SIZE
    if direction == "R":
        return (position + distance) % DIAL_SIZE
    raise ValueError(f"Unexpected direction {direction!r}")


def count_zero_positions(lines: list[str]) -> int:
    position = START_POSITION
    zero_count = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        direction, distance = parse_rotation(line)
        position = apply_rotation(position, direction, distance)
        if position == 0:
            zero_count += 1

    return zero_count


def main() -> None:
    with open(INPUT_FILE, encoding="utf-8") as f:
        lines = f.readlines()

    result = count_zero_positions(lines)
    print(result)


if __name__ == "__main__":
    main()