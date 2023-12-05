TEST_LINES = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]


def test_get_numbers() -> tuple[bool, list, list]:
    expected = [1, 21, 53, 59, 44]
    result = get_numbers("  1 21 53 59 44 ")
    return expected == result, expected, result


def test_parse_line() -> tuple[bool, dict, dict]:
    expected = {
        "winning": [1, 21, 53, 59, 44],
        "numbers": [69, 82, 63, 72, 16, 21, 14, 1]
    }
    result = parse_line(TEST_LINES[2])
    return expected == result, expected, result


def test_get_winning_count() -> tuple[bool, list, list]:
    expected = [4, 2, 2, 1, 0, 0]
    result = [get_winning_count(parse_line(line)) for line in TEST_LINES]
    return expected == result, expected, result


def test_compute_power() -> tuple[bool, list, list]:
    expected = [8, 2, 2, 1, 0, 0]
    result = [compute_power(line) for line in TEST_LINES]
    return expected == result, expected, result


def test_sum_powers() -> tuple[bool, int, int]:
    expected = 13
    result = sum_powers(TEST_LINES)
    return expected == result, expected, result


def test_parse_cards() -> tuple[bool, list, list]:
    expected = [
        {
            'copies': 1,
            'card': {
                'winning': [41, 48, 83, 86, 17],
                'numbers': [83, 86, 6, 31, 17, 9, 48, 53]}
        }
    ]

    result = parse_cards([TEST_LINES[0]])
    return expected == result, expected, result


def test_sum_won() -> tuple[bool, int, int]:
    expected = 30
    result = sum_won(TEST_LINES)
    return expected == result, expected, result


def launch_test(name: str, ok: bool, expected, result):
    if not ok:
        print(f"{name} failed: {expected} vs {result}")
    else:
        print(f"OK {name}")


def get_numbers(numbers: str) -> list[int]:
    return [int(n) for n in numbers.strip().split(" ") if n]


def parse_line(line: str) -> dict:
    numbers = line[line.find(":")+1:].split("|")
    return {
        "winning": get_numbers(numbers[0]),
        "numbers": get_numbers(numbers[1]),
    }


def get_winning_count(card: dict) -> int:
    return sum(1 for n in card["numbers"] if n in card["winning"])


def compute_power(line: str) -> int:
    winning_count = get_winning_count(parse_line(line))
    if winning_count:
        return pow(2, winning_count-1)
    return 0


def sum_powers(lines: list[str]) -> int:
    return sum(compute_power(line) for line in lines)


def parse_cards(lines: list[str]) -> list[dict]:
    return [{"copies": 1, "card": parse_line(line)} for line in lines]


def sum_won(lines: list[str]) -> int:
    cards = parse_cards(lines)
    for i, card in enumerate(cards):
        winning = get_winning_count(card["card"])
        for j in range(1, winning + 1):
            cards[i + j]["copies"] += cards[i]["copies"]
    return sum(card["copies"] for card in cards)


if __name__ == '__main__':
    launch_test("test_parse_line", *test_parse_line())
    launch_test("test_get_numbers", *test_get_numbers())
    launch_test("test_get_winning_count", *test_get_winning_count())
    launch_test("test_compute_power", *test_compute_power())
    launch_test("test_sum_powers", *test_sum_powers())

    file = open("04-01.txt")
    lines = file.read().splitlines()
    file.close()

    print(f"Part I - Result: {sum_powers(lines)}")

    launch_test("test_parse_cards", *test_parse_cards())
    launch_test("test_sum_won", *test_sum_won())

    print(f"Part II - Result: {sum_won(lines)}")
