from day_17 import (
    parse_lines,
)

f = open("test_input.txt")
TEST_LINES = f.read().splitlines()
f.close()


def test_parse_lines():
    expected = [
        [2, 4, 1, 3, 4, 3, 2, 3, 1, 1, 3, 2, 3],
        [3, 2, 1, 5, 4, 5, 3, 5, 3, 5, 6, 2, 3],
        [3, 2, 5, 5, 2, 4, 5, 6, 5, 4, 2, 5, 4],
        [3, 4, 4, 6, 5, 8, 5, 8, 4, 5, 4, 5, 2],
    ]
    result = parse_lines(TEST_LINES[:4])
    assert result == expected


def test_path_possible_moves():
    blocks = parse_lines(TEST_LINES)
    expected = [(0, 1, DOWN), (1, 0, RIGHT)]

    path = Path((0, 0), RIGHT, 0, 0, True, [])
    result = path.possible_moves(blocks)
    assert result == expected


def test_path_possible_directions():
    path = Path((0, 0), 0, 2, 0, True, [])
    expected = [UP, LEFT, RIGHT]
    result = path.possible_directions()
    assert result == expected

    path = Path((0, 0), 0, 3, 0, True, [])
    expected = [LEFT, RIGHT]
    result = path.possible_directions()
    assert result == expected

    path = Path((0, 0), 3, 0, 0, True, [])
    expected = [UP, DOWN, RIGHT]
    result = path.possible_directions()
    assert result == expected


def test_path_move():
    path = Path((0, 0), 0, 2, 0, True, [])
    path.move((0, 1), 10, 0)

    assert path.position == (0, 1)
    assert path.heat_loss == 10
    assert path.direction_count == 3
    assert path.direction == UP

    path.move((0, 2), 10, 1)

    assert path.position == (0, 2)
    assert path.heat_loss == 20
    assert path.direction_count == 1
    assert path.direction == DOWN


def test_remove_path():
    paths = [
        Path((0, 0), 0, 2, 0, True, []),
        Path((0, 1), 0, 2, 0, True, []),
        Path((0, 2), 0, 2, 0, True, []),
    ]
    expected = [(0, 0), (0, 2)]
    paths = remove_path(paths, 1)
    result = [p.position for p in paths]
    assert result == expected


def test_get_lowest_heat_loss():
    expected = 102
    result = get_lowest_heat_loss(TEST_LINES)
    assert result == expected
