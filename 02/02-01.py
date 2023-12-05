import re
from functools import reduce

CUBES_MAP = {
    "blue": 14,
    "green": 13,
    "red": 12
}

TEST_LINES = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]


def test_parse_line() -> tuple[bool, dict, dict]:
    expected = {
        "blue": 6,
        "green": 13,
        "red": 20
    }
    result = parse_line(TEST_LINES[2])
    return expected == result, expected, result


def test_parse_id() -> tuple[bool, int, int]:
    expected = 5
    result = parse_id(TEST_LINES[4])
    return expected == result, expected, result


def test_possible_game() -> tuple[bool, list[bool], list[bool]]:
    expected = [True, True, False, False, True]
    result = [possible_game(parse_line(line)) for line in TEST_LINES]
    return expected == result, expected, result


def test_sum_possible_games() -> tuple[bool, int, int]:
    expected = 8
    result = sum_possible_games(TEST_LINES)
    return expected == result, expected, result


def test_compute_line_power() -> tuple[bool, int, int]:
    expected = 1560
    result = compute_line_power(TEST_LINES[2])
    return expected == result, expected, result


def test_sum_line_power() -> tuple[bool, int, int]:
    expected = 2286
    result = sum_line_power(TEST_LINES)
    return expected == result, expected, result


def launch_test(name: str, ok: bool, expected, result):
    if not ok:
        print(f"{name} failed: {expected} vs {result}")
    else:
        print(f"OK {name}")


def parse_line(line: str) -> dict:
    pattern = r'(\d+) (blue|green|red)'
    max_cube = {
        "blue": 0,
        "green": 0,
        "red": 0
    }

    for match in re.findall(pattern, line):
        value = int(match[0])
        if value > max_cube[match[1]]:
            max_cube[match[1]] = value

    return max_cube


def parse_id(line: str) -> int:
    pattern = r'Game (\d+):'

    matches = re.findall(pattern, line)
    return int(matches[0])


def possible_game(max_cubes: dict) -> bool:
    for color, quantity in max_cubes.items():
        if quantity > CUBES_MAP[color]:
            return False
    return True


def sum_possible_games(lines: list[str]) -> int:
    return sum(parse_id(line) for line in lines if possible_game(parse_line(line)))


def compute_line_power(line: str) -> int:
    max_cube = parse_line(line)
    return reduce(lambda x, y: x * y, max_cube.values())


def sum_line_power(lines: list[str]) -> int:
    return sum(compute_line_power(line) for line in lines)


if __name__ == '__main__':
    launch_test("test_parse_line", *test_parse_line())
    launch_test("test_parse_id", *test_parse_id())
    launch_test("test_possible_game", *test_possible_game())
    launch_test("test_sum_possible_game", *test_sum_possible_games())

    file = open("02-01.txt")
    lines = file.read().splitlines()
    file.close()

    print(f"Part I - Result: {sum_possible_games(lines)}")

    launch_test("test_compute_line_power", *test_compute_line_power())
    launch_test("test_sum_line_power", *test_sum_line_power())

    print(f"Part II - Result: {sum_line_power(lines)}")





