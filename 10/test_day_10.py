import sys

from day_10 import find_loop

TEST_LINES = ["-L|F7", "7S-7|", "L|7||", "-L-J|", "L|-JF"]
TEST_LINES2 = ["7-F7-", ".FJ|7", "SJLL7", "|F--J", "LJ.LJ"]
TEST_LINES3 = [
    "...........",
    ".S-------7.",
    ".|F-----7|.",
    ".||.....||.",
    ".||.....||.",
    ".|L-7.F-J|.",
    ".|..|.|..|.",
    ".L--J.L--J.",
    "...........",
]


def test_find_loop():
    expected = 4
    result = find_loop(TEST_LINES)
    assert result == expected

    expected = 8
    result = find_loop(TEST_LINES2)
    assert result == expected

    expected = 23
    result = find_loop(TEST_LINES3)
    assert result == expected
