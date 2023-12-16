from day_16 import (
    parse_lines,
    move,
    Point,
    compute_direction,
    move_beams,
    points_to_lines,
    sum_tiles,
    Beam,
)

f = open("test_input.txt")
lines = f.read().splitlines()
TEST_LINES = lines[:10]
TEST_LINES_2 = lines[11:21]
TEST_LINES_3 = lines[22:]
f.close()


def test_parse_lines():
    expected = [
        "(0,0) 0 False",
        "(0,1) 1 False",
        "(0,2) 2 False",
        "(1,2) 3 False",
        "(0,3) 4 False",
    ]
    points = parse_lines([".", "/", "\\|", "-"])
    result = [p.__str__() for p in points]
    assert result == expected


def test_move():
    points = parse_lines(TEST_LINES)
    expected = [(1, 0), None]
    result = [move(points[0], 2, points).coordinates(), move(points[0], 3, points)]
    assert result == expected


def test_compute_direction():
    p = [
        Point(0, 0, 0, False, None),
        Point(0, 0, 1, False, None),
        Point(0, 0, 2, False, None),
        Point(0, 0, 3, False, None),
        Point(0, 0, 4, False, None),
    ]
    expected = [0, 1, 2, 0, 3]
    result = [
        compute_direction(p[0], 0),
        compute_direction(p[1], 3),
        compute_direction(p[2], 1),
        compute_direction(p[3], 0),
        compute_direction(p[4], 3),
    ]
    assert result == expected


def test_move_beams():
    expected = [
        "######....",
        ".#...#....",
        ".#...#####",
        ".#...##...",
        ".#...##...",
        ".#...##...",
        ".#..####..",
        "########..",
        ".#######..",
        ".#...#.#..",
    ]
    points = parse_lines(TEST_LINES)
    move_beams(points, Beam(Point(-1, 0, 0, False, None), 2))
    result = points_to_lines(points)
    assert result == expected


def test_sum_tiles():
    expected = 46
    result = sum_tiles(TEST_LINES)
    assert result == expected

    expected = 14
    result = sum_tiles(TEST_LINES_2)
    assert result == expected

    expected = 19
    result = sum_tiles(TEST_LINES_3)
    assert result == expected
