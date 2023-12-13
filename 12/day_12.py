import re
from dataclasses import dataclass
from functools import cache


class SpringRow:
    springs: str
    groups: list[int]
    pattern: str
    combinations: int

    def __init__(self, springs, groups):
        self.springs = "." + springs.strip(".")
        self.groups = groups
        self.combinations = 0
        self.compute_regex_pattern()

    def __str__(self):
        return f"{self.springs} {self.groups}"

    def compute_regex_pattern(self):
        self.pattern = f"^[.?]*([#?]{{{self.groups[0]}}})"
        for g in self.groups[1:]:
            self.pattern += f"[.?]+([#?]{{{g}}})"
        self.pattern += "[.?]*$"

    def compute_combinations(self, index: int, combination: str):
        if index == len(self.springs) and len(re.findall(self.pattern, combination)):
            self.combinations += 1
            return

        if not len(
            re.findall(self.pattern, combination + self.springs[len(combination) :])
        ):
            return

        curr_char = self.springs[index]
        if curr_char == "?":
            self.compute_combinations(index + 1, combination + "#")
            self.compute_combinations(index + 1, combination + ".")
        else:
            self.compute_combinations(index + 1, combination + curr_char)


def parse_lines(lines: list[str], unfold=False) -> list[SpringRow]:
    rows: list[SpringRow] = []

    for line in lines:
        springs, groups = line.split(" ")
        groups = [int(g) for g in groups.split(",")]
        if unfold:
            springs = "?".join([springs for _ in range(5)])
            groups *= 5
        rows.append(SpringRow(springs, groups))

    return rows


def sum_combinations(lines: list[str], unfold=False) -> int:
    spring_rows = parse_lines(lines, unfold)
    for s in spring_rows:
        s.compute_combinations(0, "")
    return sum(s.combinations for s in spring_rows)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
        print(f"Part I - Result: {sum_combinations(lines)}.")
        print(f"Part II - Result: {sum_combinations(lines, True)}.")
