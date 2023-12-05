def is_symbol(char: str) -> bool:
    return not char.isdigit() and char != "."


def is_outside(x: int, y: int, lines: list[str]):
    return y < 0 or y >= len(lines) or x < 0 or x >= len(lines[y])


def get_number(x: int, y: int, lines: list[str]) -> int:
    number = ""
    while not is_outside(x-1, y, lines) and lines[y][x-1].isdigit():
        x -= 1
    while not is_outside(x, y, lines) and lines[y][x].isdigit():
        number += lines[y][x]
        lines[y] = lines[y][:x] + "." + lines[y][x+1:]
        x += 1
    return int(number)


def catch_number(x: int, y: int, lines: list[str]) -> int:
    if not is_outside(x, y, lines) and lines[y][x].isdigit():
        return get_number(x, y, lines)
    return 0


def sum_numbers(x: int, y: int, lines) -> int:
    return sum([catch_number(x + dx, y + dy, lines) for dx in range(-1, 2) for dy in range(-1, 2) if (dx, dy) != (0, 0)])


def iterate_through_map(lines: list[str]):
    numbers_sum = 0
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            if is_symbol(lines[y][x]):
                numbers_sum += sum_numbers(x, y, lines)
    return numbers_sum


if __name__ == '__main__':
    file = open("03.txt")
    lines = file.read().splitlines()
    file.close()
    print(f"Part I - Result: {iterate_through_map(lines)}")