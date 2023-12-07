from day_07 import Hand, parse_hands, rank_hands, sum_scores

TEST_LINES = ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]


def test_get_hand_type():
    expected = [1, 3, 2, 2, 3, 4, 4, 5, 6, 0]
    hands = [
        Hand("32T3K", 0),
        Hand("T55J5", 0),
        Hand("KK677", 0),
        Hand("KTJJT", 0),
        Hand("QQQJA", 0),
        Hand("QQQJJ", 0),
        Hand("QJQQJ", 0),
        Hand("QQQJQ", 0),
        Hand("QQQQQ", 0),
        Hand("23456", 0),
    ]
    result = [h.get_hand_type() for h in hands]
    assert result == expected

    expected = [1, 5, 2, 5, 5, 6, 6, 6, 6, 0]
    hands = [
        Hand("32T3K", 0, True),
        Hand("T55J5", 0, True),
        Hand("KK677", 0, True),
        Hand("KTJJT", 0, True),
        Hand("QQQJA", 0, True),
        Hand("QQQJJ", 0, True),
        Hand("QJQQJ", 0, True),
        Hand("QQQJQ", 0, True),
        Hand("QQQQQ", 0, True),
        Hand("23456", 0, True),
    ]
    result = [h.get_hand_type() for h in hands]
    assert result == expected


def test_parse_hands():
    expected = [
        Hand("32T3K", 765),
        Hand("T55J5", 684),
        Hand("KK677", 28),
        Hand("KTJJT", 220),
        Hand("QQQJA", 483),
    ]
    result = parse_hands(TEST_LINES)
    for i in range(0, len(expected)):
        assert result[i].__str__() == expected[i].__str__()


def test_rank_hands():
    hands = parse_hands(TEST_LINES)
    expected = [1, 4, 3, 2, 5]
    rank_hands(hands)
    result = [h.rank for h in hands]
    assert result == expected

    hands = [
        Hand("33155", 0),
        Hand("A234J", 0),
        Hand("2A34J", 0),
        Hand("33244", 0),
        Hand("JJJJJ", 0),
    ]
    rank_hands(hands)
    expected = [3, 2, 1, 4, 5]
    result = [h.rank for h in hands]
    assert result == expected


def test_sum_scores():
    expected = 6440
    result = sum_scores(TEST_LINES)
    assert result == expected

    expected = 5905
    result = sum_scores(TEST_LINES, True)
    assert result == expected
