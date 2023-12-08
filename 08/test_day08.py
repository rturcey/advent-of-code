from day_08 import parse_instructions, parse_lines, count_steps

TEST_LINES = [
    "RL",
    "",
    "AAA = (BBB, CCC)",
    "BBB = (DDD, EEE)",
    "CCC = (ZZZ, GGG)",
    "DDD = (DDD, DDD)",
    "EEE = (EEE, EEE)",
    "GGG = (GGG, GGG)",
    "ZZZ = (ZZZ, ZZZ)",
]

TEST_LINES2 = ["LLR", "", "AAA = (BBB, BBB)", "BBB = (AAA, ZZZ)", "ZZZ = (ZZZ, ZZZ)"]


def test_parse_instructions():
    expected = [1, 0]
    result = parse_instructions(TEST_LINES[0])
    assert result == expected


def test_parse_lines():
    expected = [1, 0], {
        "AAA": ["BBB", "CCC"],
        "BBB": ["DDD", "EEE"],
        "CCC": ["ZZZ", "GGG"],
        "DDD": ["DDD", "DDD"],
        "EEE": ["EEE", "EEE"],
        "GGG": ["GGG", "GGG"],
        "ZZZ": ["ZZZ", "ZZZ"],
    }
    result = parse_lines(TEST_LINES)
    assert result == expected


def test_count_steps():
    expected = 2
    result = count_steps(TEST_LINES)
    assert result == expected

    expected = 6
    result = count_steps(TEST_LINES2)
    assert result == expected
