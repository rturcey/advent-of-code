from day_05 import (
    Equivalence,
    parse_seeds,
    get_equivalences,
    parse_name,
    apply_equivalences,
    compute_locations,
    get_lowest_location,
)

file = open("test_input.txt")
TEST_LINES = file.read().splitlines()
file.close()


def test_equivalence_append_to_map():
    expected = [{"src_start": 98, "src_stop": 100, "dst_start": 50, "length": 2}]
    equivalence = Equivalence("seed-to-soil")
    equivalence.append_to_map(TEST_LINES[3])
    result = equivalence.conversion_map
    assert result == expected


def test_get_equivalences():
    expected = {
        98: 50,
        99: 51,
        50: 52,
        51: 53,
        52: 54,
        53: 55,
        54: 56,
        55: 57,
        56: 58,
        57: 59,
        58: 60,
        59: 61,
        60: 62,
        61: 63,
        62: 64,
        63: 65,
        64: 66,
        65: 67,
        66: 68,
        67: 69,
        68: 70,
        69: 71,
        70: 72,
        71: 73,
        72: 74,
        73: 75,
        74: 76,
        75: 77,
        76: 78,
        77: 79,
        78: 80,
        79: 81,
        80: 82,
        81: 83,
        82: 84,
        83: 85,
        84: 86,
        85: 87,
        86: 88,
        87: 89,
        88: 90,
        89: 91,
        90: 92,
        91: 93,
        92: 94,
        93: 95,
        94: 96,
        95: 97,
        96: 98,
        97: 99,
    }
    equivalences = get_equivalences(TEST_LINES)
    assert len(equivalences) == 7


def test_equivalence_convert():
    expected = [81, 14, 57, 13]
    seeds = [79, 14, 55, 13]
    equivalence = Equivalence("seed-to-soil")
    equivalence.append_to_map(TEST_LINES[3])
    equivalence.append_to_map(TEST_LINES[4])
    result = [equivalence.convert(s) for s in seeds]
    assert result == expected


def test_parse_seeds():
    expected = [79, 14, 55, 13]
    result = parse_seeds(TEST_LINES)
    assert result == expected


def test_parse_name():
    expected = "seed-to-soil"
    result = parse_name(TEST_LINES[2])
    assert result == expected


def test_apply_equivalences():
    expected = 82
    equivalences = get_equivalences(TEST_LINES)
    seed = 79
    result = apply_equivalences(seed, equivalences)
    assert result == expected


def test_compute_locations():
    expected = [82, 43, 86, 35]
    result = compute_locations(TEST_LINES)
    assert result == expected


def test_get_lowest_location():
    expected = 35
    result = get_lowest_location(TEST_LINES)
    assert result == expected
