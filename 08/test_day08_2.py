from day_08_2 import (
    parse_instructions,
    parse_lines,
    get_first_count,
    count_all_z,
)

TEST_LINES = [
    "LR",
    "",
    "11A = (11B, XXX)",
    "11B = (XXX, 11Z)",
    "11Z = (11B, XXX)",
    "22A = (22B, XXX)",
    "22B = (22C, 22C)",
    "22C = (22Z, 22Z)",
    "22Z = (22B, 22B)",
    "XXX = (XXX, XXX)",
]


def test_parse_instructions():
    expected = [0, 1]
    result = parse_instructions(TEST_LINES[0])
    assert result == expected


def test_parse_lines():
    expected = [0, 1], {
        "11A": ["11B", "XXX"],
        "11B": ["XXX", "11Z"],
        "11Z": ["11B", "XXX"],
        "22A": ["22B", "XXX"],
        "22B": ["22C", "22C"],
        "22C": ["22Z", "22Z"],
        "22Z": ["22B", "22B"],
        "XXX": ["XXX", "XXX"],
    }
    result = parse_lines(TEST_LINES)
    assert result == expected


def test_get_first_count():
    expected = 2
    instructions, networks = parse_lines(TEST_LINES)
    result = get_first_count(instructions, networks, "11A")
    assert result == expected

    expected = 3
    instructions, networks = parse_lines(TEST_LINES)
    result = get_first_count(instructions, networks, "22A")
    assert result == expected


def test_count_all_z():
    expected = 6
    result = count_all_z(TEST_LINES)
    assert result == expected
