from day_13 import parse_lines, col_to_rows, find_mirror, sum_repeated

TEST_LINES = [
    "#.##..##.",
    "..#.##.#.",
    "##......#",
    "##......#",
    "..#.##.#.",
    "..##..##.",
    "#.#.##.#.",
    "",
    "#...##..#",
    "#....#..#",
    "..##..###",
    "#####.##.",
    "#####.##.",
    "..##..###",
    "#....#..#",
]

TEST_LINES_BIS = [
    "##....###.#..",
    "########...#.",
    "##.##.##.#.##",
    "........###.#",
    "........#.#.#",
    "#######.###..",
    ".#.##.#.#....",
    "..####..##..#",
    "##.##.##.##.#",
    "##.##.##.##.#",
    "..####..##..#",
    ".#.##.#.#....",
    "#######.###..",
    "........#.#.#",
    "........###.#",
    "",
    "#.###..#..###",
    ".#...##.####.",
    ".#...##.####.",
    "#.###..#..###",
    ".#######.##.#",
    ".#..##.#.#..#",
    "..#..#.##.#..",
    "##..##..###.#",
    "######.##..#.",
    "######.##....",
    "##..##..###.#",
    "..#..#.##.#..",
    ".#..##.#.#..#",
]


def test_parse_lines():
    expected = [
        [
            "#.##..##.",
            "..#.##.#.",
            "##......#",
            "##......#",
            "..#.##.#.",
            "..##..##.",
            "#.#.##.#.",
        ],
        [
            "#...##..#",
            "#....#..#",
            "..##..###",
            "#####.##.",
            "#####.##.",
            "..##..###",
            "#....#..#",
        ],
    ]
    result = parse_lines(TEST_LINES)
    assert result == expected


def test_col_to_rows():
    expected = [
        "#.##..#",
        "..##...",
        "##..###",
        "#....#.",
        ".#..#.#",
        ".#..#.#",
        "#....#.",
        "##..###",
        "..##...",
    ]
    result = col_to_rows(parse_lines(TEST_LINES)[0])
    assert result == expected


def test_find_mirror():
    expected = [-1, 4]
    result = [find_mirror(p, False, (), []) for p in parse_lines(TEST_LINES)]
    assert result == expected


def test_sum_repeated():
    expected = 405
    result, _ = sum_repeated(TEST_LINES, [])
    assert result == expected


def test_sum_repeated_p2():
    expected = 400
    result, lines = sum_repeated(TEST_LINES, [])
    result, lines = sum_repeated(TEST_LINES, lines, True)
    assert result == expected


def test_sum_repeated_p2bis():
    expected = 2300
    result, lines = sum_repeated(TEST_LINES_BIS, [])
    print("\n".join(TEST_LINES_BIS))
    result, lines = sum_repeated(TEST_LINES_BIS, lines, True)
    assert result == expected
