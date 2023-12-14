from dataclasses import dataclass
from functools import cache

CUBE_ROCK = "#"
ROUNDED_ROCK = "O"
EMPTY = "."


@cache
def slide(line: str, max: int) -> str:
    cube_indexes = [-1] + [i for i, c in enumerate(line) if c == CUBE_ROCK] + [max]
    line_parts: list[str] = []
    for i in range(len(cube_indexes) - 1):
        line_part = line[cube_indexes[i] + 1 : cube_indexes[i + 1]]
        rounded_count = line_part.count(ROUNDED_ROCK)
        empty_count = len(line_part) - rounded_count
        line_part = ROUNDED_ROCK * rounded_count + EMPTY * empty_count
        line_parts.append(line_part)
    return "#".join(line_parts)


def slide_row(platform: list[str], y: int, reverse=False):
    row = platform[y]
    if reverse:
        row = row[::-1]

    row = slide(row, len(platform))

    if reverse:
        row = row[::-1]
    platform[y] = row


def slide_column(platform: list[str], x: int, reverse=False):
    column = ""
    for y in range(len(platform)):
        column += platform[y][x]

    if reverse:
        column = column[::-1]

    column = slide(column, len(platform))

    if reverse:
        column = column[::-1]

    for i, c in enumerate(column):
        end = ""
        if x < len(platform[0]) - 1:
            end = platform[i][x + 1 :]
        platform[i] = platform[i][:x] + c + end


@cache
def compute_cycle(platform_str: str) -> list[str]:
    platform = platform_str.split("|")
    for x in range(len(platform[0])):
        slide_column(platform, x)
    for y in range(len(platform)):
        slide_row(platform, y)
    for x in range(len(platform[0])):
        slide_column(platform, x, True)
    for y in range(len(platform)):
        slide_row(platform, y, True)
    return platform


def count_platform(platform: list[str]) -> int:
    count = 0
    for i, row in enumerate(platform):
        count += row.count(ROUNDED_ROCK) * (len(platform) - i)
    return count


def slide_platform_north(platform: list[str]) -> int:
    for x in range(len(platform[0])):
        slide_column(platform, x)

    return count_platform(platform)


def compute_multiple_cycle(platform: list[str], repetitions: int) -> int:
    cache = {}
    i = 0
    while i < repetitions:
        str_platform = "|".join(platform)
        platform = compute_cycle(str_platform)

        if str_platform in cache:
            back = i - cache[str_platform]
            still = int((repetitions - i) / back)
            i += back * still
        else:
            cache[str_platform] = i
        i += 1

    return count_platform(platform)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
        print(f"Part I - Result: {slide_platform_north(lines)}.")
        print(f"Part II - Result: {compute_multiple_cycle(lines, 1000000000)}.")
