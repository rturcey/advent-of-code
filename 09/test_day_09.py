from day_09 import Sequence, sum_last_of_first_sequences

TEST_LINES = ["0 3 6 9 12 15", "1 3 6 10 15 21", "10 13 16 21 30 45"]


def test_compute_subsequences():
    expected = [
        [
            [0, 3, 6, 9, 12, 15],
            [3, 3, 3, 3, 3],
            [0, 0, 0, 0],
        ],
        [[1, 3, 6, 10, 15, 21], [2, 3, 4, 5, 6], [1, 1, 1, 1], [0, 0, 0]],
        [[10, 13, 16, 21, 30, 45], [3, 3, 5, 9, 15], [0, 2, 4, 6], [2, 2, 2], [0, 0]],
    ]
    sequences = [Sequence(line) for line in TEST_LINES]
    result = [s.sequences for s in sequences]
    assert result == expected


def test_increment_sequences():
    sequences = [Sequence(line) for line in TEST_LINES]
    for s in sequences:
        s.increment_sequences()
    expected = [
        [
            [0, 3, 6, 9, 12, 15, 18],
            [3, 3, 3, 3, 3, 3],
            [0, 0, 0, 0],
        ],
        [[1, 3, 6, 10, 15, 21, 28], [2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1], [0, 0, 0]],
        [
            [10, 13, 16, 21, 30, 45, 68],
            [3, 3, 5, 9, 15, 23],
            [0, 2, 4, 6, 8],
            [2, 2, 2, 2],
            [0, 0],
        ],
    ]
    result = [s.sequences for s in sequences]
    assert result == expected


def test_increment_sequences_backward():
    sequences = [Sequence(line) for line in TEST_LINES]
    for s in sequences:
        s.increment_sequences_backward()
    expected = [
        [
            [-3, 0, 3, 6, 9, 12, 15],
            [3, 3, 3, 3, 3, 3],
            [0, 0, 0, 0],
        ],
        [[0, 1, 3, 6, 10, 15, 21], [1, 2, 3, 4, 5, 6], [1, 1, 1, 1, 1], [0, 0, 0]],
        [
            [5, 10, 13, 16, 21, 30, 45],
            [5, 3, 3, 5, 9, 15],
            [-2, 0, 2, 4, 6],
            [2, 2, 2, 2],
            [0, 0],
        ],
    ]
    result = [s.sequences for s in sequences]
    assert result == expected


def test_sum_last_of_first_sequences():
    expected = 114
    result = sum_last_of_first_sequences(TEST_LINES)
    assert result == expected


def test_sum_first_of_first_sequences():
    expected = 114
    result = sum_last_of_first_sequences(TEST_LINES)
    assert result == expected
