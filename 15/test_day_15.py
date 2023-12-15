from day_15 import run_hash, sum_hashes, sum_focusing_power, Box, perform_sequence

TEST_LINE = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

TEST_STEPS = [
    ["Box 0: [rn 1]"],
    ["Box 0: [rn 1]"],
    ["Box 0: [rn 1]", "Box 1: [qp 3]"],
    ["Box 0: [rn 1] [cm 2]", "Box 1: [qp 3]"],
    ["Box 0: [rn 1] [cm 2]"],
    ["Box 0: [rn 1] [cm 2]", "Box 3: [pc 4]"],
    ["Box 0: [rn 1] [cm 2]", "Box 3: [pc 4] [ot 9]"],
    ["Box 0: [rn 1] [cm 2]", "Box 3: [pc 4] [ot 9] [ab 5]"],
    ["Box 0: [rn 1] [cm 2]", "Box 3: [ot 9] [ab 5]"],
    ["Box 0: [rn 1] [cm 2]", "Box 3: [ot 9] [ab 5] [pc 6]"],
    ["Box 0: [rn 1] [cm 2]", "Box 3: [ot 7] [ab 5] [pc 6]"],
]


def test_run_hash():
    expected = 52
    result = run_hash("HASH")
    assert result == expected


def test_sum_hashes():
    expected = 1320
    result = sum_hashes(TEST_LINE)
    assert result == expected


def test_perform_sequence():
    sequences = TEST_LINE.split(",")
    boxes = [Box(i) for i in range(256)]
    for i, s in enumerate(sequences):
        perform_sequence(s, boxes)
        assert [b.__str__() for b in boxes if b.lenses] == TEST_STEPS[i]


def test_sum_focusing_power():
    expected = 145
    result = sum_focusing_power(TEST_LINE)
    assert result == expected
