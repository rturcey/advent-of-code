from day_14 import (
    slide_column,
    slide_platform_north,
    slide_row,
    compute_cycle,
    compute_multiple_cycle,
    count_platform,
)

TEST_LINES = [
    "O....#....",
    "O.OO#....#",
    ".....##...",
    "OO.#O....O",
    ".O.....O#.",
    "O.#..O.#.#",
    "..O..#O..O",
    ".......O..",
    "#....###..",
    "#OO..#....",
]

TEST_LINES_2 = [
    "O....#....",
    "O.OO#....#",
    ".....##...",
    "OO.#O....O",
    ".O.....O#.",
    "O.#..O.#.#",
    "..O..#O..O",
    ".......O..",
    "#....###..",
    "#OO..#....",
]

TEST_LINES_3 = [
    "O....#....",
    "O.OO#....#",
    ".....##...",
    "OO.#O....O",
    ".O.....O#.",
    "O.#..O.#.#",
    "..O..#O..O",
    ".......O..",
    "#....###..",
    "#OO..#....",
]

TEST_1_CYCLE = [
    ".....#....",
    "....#...O#",
    "...OO##...",
    ".OO#......",
    ".....OOO#.",
    ".O#...O#.#",
    "....O#....",
    "......OOOO",
    "#...O###..",
    "#..OO#....",
]

TEST_2_CYCLE = [
    ".....#....",
    "....#...O#",
    ".....##...",
    "..O#......",
    ".....OOO#.",
    ".O#...O#.#",
    "....O#...O",
    ".......OOO",
    "#..OO###..",
    "#.OOO#...O",
]

TEST_3_CYCLE = [
    ".....#....",
    "....#...O#",
    ".....##...",
    "..O#......",
    ".....OOO#.",
    ".O#...O#.#",
    "....O#...O",
    ".......OOO",
    "#...O###.O",
    "#.OOO#...O",
]


def test_slide_column_north():
    expected = [
        "O.O..#....",
        "O..O#....#",
        ".....##...",
        "OO.#O....O",
        ".O.....O#.",
        "O.#..O.#.#",
        "..O..#O..O",
        "..O....O..",
        "#....###..",
        "#O...#....",
    ]
    slide_column(TEST_LINES, 2)
    assert TEST_LINES == expected


def test_slide_column_south():
    expected = [
        "O....#....",
        "O..O#....#",
        ".....##...",
        "OO.#O....O",
        ".OO....O#.",
        "O.#..O.#.#",
        ".....#O..O",
        ".......O..",
        "#.O..###..",
        "#OO..#....",
    ]
    slide_column(TEST_LINES, 2, True)
    assert TEST_LINES == expected


def test_slide_row_west():
    expected = [
        "O....#....",
        "O..O#....#",
        ".....##...",
        "OO.#O....O",
        ".OO....O#.",
        "O.#O...#.#",
        ".....#O..O",
        ".......O..",
        "#.O..###..",
        "#OO..#....",
    ]
    slide_row(TEST_LINES, 5)
    assert TEST_LINES == expected


def test_slide_row_east():
    expected = [
        "O....#....",
        "O..O#....#",
        ".....##...",
        "OO.#O....O",
        ".OO....O#.",
        ".O#...O#.#",
        ".....#O..O",
        ".......O..",
        "#.O..###..",
        "#OO..#....",
    ]
    slide_row(TEST_LINES, 5, True)
    assert TEST_LINES == expected


def test_slide_platform_north():
    expected = 136
    result = slide_platform_north(TEST_LINES_2)
    assert result == expected


def test_compute_cycle():
    expected = TEST_1_CYCLE
    platform = TEST_LINES_3
    compute_cycle(platform)
    assert platform == expected

    expected = TEST_2_CYCLE
    compute_cycle(platform)
    assert platform == expected

    expected = TEST_3_CYCLE
    compute_cycle(platform)
    assert platform == expected


def test_count_platform():
    expected = 69
    result = count_platform(TEST_3_CYCLE)
    assert result == expected


def test_compute_multiple_cycle():
    expected = 69
    result = compute_multiple_cycle(TEST_LINES, 3)
    assert result == expected
