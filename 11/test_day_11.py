from day_11 import (
    empty_column,
    empty_line,
    add_column,
    get_indexes_to_expand,
    get_galaxies,
    Galaxy,
    compute_shortest_path,
    get_shortest_paths_sum,
)

TEST_LINES = [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#.....",
]

TEST_LINES2 = [
    "....#........",
    ".........#...",
    "#............",
    ".............",
    ".............",
    "........#....",
    ".#...........",
    "............#",
    ".............",
    ".............",
    ".........#...",
    "#....#.......",
]


def test_add_column():
    expected = [
        ".*..*.",
        "......",
        "......",
        ".*..*.",
    ]
    lines = [
        ".*.*.",
        ".....",
        ".....",
        ".*.*.",
    ]
    add_column(lines, 3)
    assert lines == expected


def test_empty_column():
    expected = [False, False, True]
    result = [empty_column(TEST_LINES, i) for i in range(0, 3)]
    assert result == expected


def test_empty_line():
    expected = [False, False, False, True]
    result = [empty_line(TEST_LINES[i]) for i in range(0, 4)]
    assert result == expected


def test_get_indexes_to_expand():
    expected = {"rows": [3, 7], "columns": [2, 5, 8]}
    result = get_indexes_to_expand(TEST_LINES)
    assert result == expected


def test_get_galaxies():
    expected = [
        "1: 4,0",
        "2: 9,1",
        "3: 0,2",
        "4: 8,5",
        "5: 1,6",
        "6: 12,7",
        "7: 9,10",
        "8: 0,11",
        "9: 5,11",
    ]
    result = [
        g.__str__()
        for g in get_galaxies(TEST_LINES, get_indexes_to_expand(TEST_LINES), 2)
    ]
    assert result == expected


def test_compute_shortest_path():
    expected = [9, 15, 17, 5]
    g = [
        Galaxy(1, 6, 5),
        Galaxy(5, 11, 9),
        Galaxy(4, 0, 1),
        Galaxy(9, 10, 7),
        Galaxy(0, 2, 3),
        Galaxy(12, 7, 6),
        Galaxy(0, 11, 8),
    ]
    result = [
        compute_shortest_path(g[0], g[1]),
        compute_shortest_path(g[2], g[3]),
        compute_shortest_path(g[4], g[5]),
        compute_shortest_path(g[6], g[1]),
    ]

    assert result == expected


def test_get_shortest_path_sum():
    result = 374
    expected = get_shortest_paths_sum(TEST_LINES, 2)
    assert result == expected

    result = 1030
    expected = get_shortest_paths_sum(TEST_LINES, 10)
    assert result == expected

    result = 8410
    expected = get_shortest_paths_sum(TEST_LINES, 100)
    assert result == expected
