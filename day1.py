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
    """Part 1: count times the dial is at 0 after completing a rotation."""
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


def count_zero_clicks(lines: list[str]) -> int:
    """Part 2 (method 0x434C49434B): count all clicks that land on 0."""
    position = START_POSITION
    zero_clicks = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        direction, distance = parse_rotation(line)

        if direction == "R":
            # Solve position + k ≡ 0 (mod DIAL_SIZE) for k in [1, distance]
            k0 = (-position) % DIAL_SIZE
        else:  # direction == "L"
            # Solve position - k ≡ 0 (mod DIAL_SIZE) -> k ≡ position (mod DIAL_SIZE)
            k0 = position % DIAL_SIZE

        # k0 == 0 means the first time we hit 0 is after DIAL_SIZE clicks
        if k0 == 0:
            k0 = DIAL_SIZE

        if distance >= k0:
            zero_clicks += 1 + (distance - k0) // DIAL_SIZE

        position = apply_rotation(position, direction, distance)

    return zero_clicks


def main() -> None:
    with open(INPUT_FILE, encoding="utf-8") as f:
        lines = f.readlines()

    part1 = count_zero_positions(lines)
    part2 = count_zero_clicks(lines)
    print(part1)
    print(part2)


if __name__ == "__main__":
    main()