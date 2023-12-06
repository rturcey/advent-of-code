from day_06 import parse_races, Race, winning_race, sum_winning_races

TEST_LINES = ["Time:      7  15   30", "Distance:  9  40  200"]


def test_parse_races():
    expected = [
        Race(7, 9),
        Race(15, 40),
        Race(30, 200),
    ]
    result = parse_races(TEST_LINES)
    assert result == expected


def test_parse_races_part2():
    expected = [
        Race(71530, 940200),
    ]
    result = parse_races(TEST_LINES, True)
    assert result == expected


def test_winning_race():
    race = Race(7, 9)
    expected = [False, False, True, True, True, True, False, False]
    result = [winning_race(h, race) for h in range(0, 8)]
    assert result == expected


def test_sum_winning_races():
    expected = 288
    result = sum_winning_races(TEST_LINES)
    assert result == expected


def test_sum_winning_races_part2():
    expected = 71503
    result = sum_winning_races(TEST_LINES, True)
    assert result == expected
