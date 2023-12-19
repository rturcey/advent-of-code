from day_19 import (
    Workflow,
    parse_workflows,
    parse_ratings,
    parse_lines,
    process_workflows,
    ConditionGroup,
    Condition,
    process_combinations,
)

f = open("test_input.txt")
TEST_LINES = f.read().splitlines()


def test_parse_workflow():
    expected = ["px", "a<2006:qkq", "m>2090:A", "rfg"]
    workflow = Workflow(TEST_LINES[0])
    result = [workflow.name] + [c.__str__() for c in workflow.conditions]
    assert result == expected


def test_parse_workflows():
    expected = [
        "px",
        "pv",
        "lnx",
        "rfg",
        "qs",
        "qkq",
        "crn",
        "in",
        "qqz",
        "gd",
        "hdj",
    ]
    workflows_dict = parse_workflows(TEST_LINES[:11])
    assert list(workflows_dict.keys()) == expected

    expected = TEST_LINES[:11]
    result = [w.__str__() for w in workflows_dict.values()]
    assert result == expected


def test_parse_ratings():
    expected = TEST_LINES[12:]
    result = [g.__str__() for g in parse_ratings(TEST_LINES[12:])]
    assert result == expected


def test_parse_lines():
    expected = TEST_LINES
    result = parse_lines(TEST_LINES)
    result = (
        [w.__str__() for w in result[0].values()]
        + [""]
        + [g.__str__() for g in result[1]]
    )
    assert result == expected


def test_rating_group():
    wk, rg = parse_lines(TEST_LINES)
    wk["in"].test_rating_group(rg[0])
    assert rg[0].current_workflow == "qqz"

    wk["qqz"].test_rating_group(rg[0])
    assert rg[0].current_workflow == "qs"

    wk["qs"].test_rating_group(rg[0])
    assert rg[0].current_workflow == "lnx"

    wk["lnx"].test_rating_group(rg[0])
    assert rg[0].current_workflow == "A"


def test_get_score():
    expected = 787 + 2655 + 1222 + 2876
    _, rg = parse_lines(TEST_LINES)
    result = rg[0].get_score()
    assert result == expected


def test_process_workflows():
    expected = 19114
    result = process_workflows(TEST_LINES)
    assert result == expected


def test_add_interval():
    expected = {"a": (1, 193)}
    condition_group = ConditionGroup()
    condition = Condition("a", "<", 194, "test")
    condition_group.add_interval(condition)
    assert condition_group.intervals == expected


def test_add_condition():
    expected = {"a": (1, 193)}
    condition_group = ConditionGroup()
    condition = Condition("a", "<", 194, "test")
    condition_group.add_condition(condition)
    assert condition_group.intervals == expected

    expected = {"a": (1, 191)}
    condition = Condition("a", "<", 192, "test")
    condition_group.add_condition(condition)
    assert condition_group.intervals == expected

    expected = {"a": (181, 191)}
    condition = Condition("a", ">", 180, "test")
    condition_group.add_condition(condition)
    assert condition_group.intervals == expected


def test_process_combinations():
    expected = 167409079868000
    result = process_combinations(TEST_LINES)
    assert result == expected
