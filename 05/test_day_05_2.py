import threading

from day_05_2 import (
    Equivalence,
    parse_seeds,
    get_equivalences,
    parse_name,
    apply_equivalences,
    Range,
    get_lowest_location,
    in_seeds,
)

file = open("test_input.txt")
TEST_LINES = file.read().splitlines()
file.close()


def test_equivalence_append_to_map():
    expected = [Range(src=50, dst=98, range=2)]
    equivalence = Equivalence("seed-to-soil")
    equivalence.append_to_map(TEST_LINES[3])
    result = equivalence.ranges
    assert result == expected


def test_equivalence_convert():
    expected = [79, 14, 55, 13]
    soils = [81, 14, 57, 13]
    equivalence = Equivalence("seed-to-soil")
    equivalence.append_to_map(TEST_LINES[3])
    equivalence.append_to_map(TEST_LINES[4])
    result = [equivalence.convert(s) for s in soils]
    assert result == expected


def test_parse_seeds_part1():
    expected = [
        Range(src=79, dst=79, range=1),
        Range(src=14, dst=14, range=1),
        Range(src=55, dst=55, range=1),
        Range(src=13, dst=13, range=1),
    ]
    result = parse_seeds(TEST_LINES, True)
    assert result == expected


def test_parse_seeds():
    expected = [Range(src=55, dst=55, range=13), Range(src=79, dst=79, range=14)]
    result = parse_seeds(TEST_LINES)
    assert result == expected


def test_in_seeds():
    seeds = parse_seeds(TEST_LINES)
    expected = [False, True, False, True]
    result = [in_seeds(n, seeds) for n in [78, 79, 100, 82]]
    assert result == expected


def test_parse_name():
    expected = "seed-to-soil"
    result = parse_name(TEST_LINES[2])
    assert result == expected


def test_apply_equivalences():
    expected = 13
    equivalences = get_equivalences(TEST_LINES)
    location = 35
    result = apply_equivalences(location, equivalences)
    assert result == expected


def test_get_lowest_location():
    expected = 46
    equivalences = get_equivalences(TEST_LINES)
    seeds = parse_seeds(TEST_LINES)
    result = get_lowest_location(0, 50, equivalences, seeds, [])
    assert result == expected


def test_get_lowest_location_part1():
    expected = 35
    equivalences = get_equivalences(TEST_LINES)
    seeds = parse_seeds(TEST_LINES, True)
    result = get_lowest_location(0, 50, equivalences, seeds, [])
    assert result == expected
