import re
from dataclasses import dataclass
from heapq import heapify, heappop, heappush


@dataclass
class Rating:
    item: str
    score: int

    def __str__(self):
        return f"{self.item}={self.score}"


@dataclass
class RatingGroup:
    ratings: list[Rating]
    current_workflow: str = "in"
    processed: int = 0

    def get_item(self, item: str):
        return [r for r in self.ratings if r.item == item][0]

    def get_score(self):
        return sum(r.score for r in self.ratings)

    def __str__(self):
        ratings = [r.__str__() for r in self.ratings]
        return f"{{{','.join(ratings)}}}"

    def __lt__(self, other):
        return self.processed < other.processed


@dataclass
class Condition:
    item: str
    operator: str
    condition: int
    destination: str

    def is_dest(self) -> bool:
        return False if self.item else True

    def __str__(self):
        return (
            f"{self.item}{self.operator}{self.condition}:{self.destination}"
            if self.item
            else f"{self.destination}"
        )


class ConditionGroup:
    def __init__(self):
        self.intervals: dict = {}
        self.current_workflow: str = "in"

    def add_interval(self, c: Condition):
        if c.operator == "<":
            self.intervals[c.item] = (1, c.condition - 1)
        else:
            self.intervals[c.item] = (c.condition + 1, 4000)

    def add_condition(self, c: Condition) -> bool:
        if c.is_dest():
            self.current_workflow = c.destination
            return True

        if not c.item in self.intervals:
            self.add_interval(c)
            return True

        if (
            c.operator == "<"
            and self.intervals[c.item][0] <= c.condition - 1 < self.intervals[c.item][1]
        ):
            self.intervals[c.item] = (self.intervals[c.item][0], c.condition - 1)
            return True
        if (
            c.operator == ">"
            and self.intervals[c.item][0] < c.condition + 1 <= self.intervals[c.item][1]
        ):
            self.intervals[c.item] = (c.condition + 1, self.intervals[c.item][1])
            return True

        return False

    def __lt__(self, other):
        return len(self.intervals) < len(other.intervals)

    def __str__(self):
        return self.intervals.__str__()


class Workflow:
    def __init__(self, line: str):
        split_line = line.strip("}").split("{")

        self.name = split_line[0]
        self.conditions: list[Condition] = []

        self.parse_workflow(split_line[1])

    def parse_workflow(self, line: str):
        pattern = r"((([xmas]{1})([<>]{1})(\d+))):([a-zAR]+)|([a-zAR]+)"
        matches = re.findall(pattern, line)
        for m in matches:
            self.conditions.append(
                Condition(m[2], m[3], int(m[4]) if m[4] else "", m[5] if m[5] else m[6])
            )
        return

    def test_rating_group(self, rating_group: RatingGroup):
        for c in self.conditions:
            if c.is_dest():
                rating_group.current_workflow = c.destination
                return
            item = rating_group.get_item(c.item)
            result = (
                item.score < c.condition
                if c.operator == "<"
                else item.score > c.condition
            )
            if result:
                rating_group.current_workflow = c.destination
                return

    def __str__(self):
        conditions = [c.__str__() for c in self.conditions]
        return f"{self.name}{{{','.join(conditions)}}}"


def parse_workflows(lines: list[str]) -> dict:
    workflows = {}
    for line in lines:
        workflow = Workflow(line)
        workflows[workflow.name] = workflow
    return workflows


def parse_ratings(lines: list[str]) -> list[RatingGroup]:
    pattern = r"([xmas]{1})=(\d+)"
    rating_groups: list[RatingGroup] = []

    for line in lines:
        matches = re.findall(pattern, line)
        ratings = [Rating(m[0], int(m[1])) for m in matches]
        rating_groups.append(RatingGroup(ratings))

    return rating_groups


def parse_lines(lines: list[str]) -> tuple[dict, list[RatingGroup]]:
    empty_line = lines.index("")
    return (
        parse_workflows(lines[:empty_line]),
        parse_ratings(lines[empty_line + 1 :]),
    )


def process_workflows(lines: list[str]) -> int:
    workflow_dict, rating_groups = parse_lines(lines)
    score = 0
    heapify(rating_groups)

    while len(rating_groups):
        rg = heappop(rating_groups)
        workflow_dict[rg.current_workflow].test_rating_group(rg)
        rg.processed += 1
        if rg.current_workflow == "A":
            score += rg.get_score()
            continue
        elif rg.current_workflow == "R":
            continue
        heappush(rating_groups, rg)

    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
        print(f"Part I - Result: {process_workflows(lines)}.")
