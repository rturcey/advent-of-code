import re
from dataclasses import dataclass


class Equivalence:
    def __init__(self, name: str):
        self.name = name
        self.conversion_map: list[dict] = []

    def append_to_map(self, line: str):
        numbers = [int(n) for n in line.split(" ")]
        dst_start, src_start, length = numbers[0], numbers[1], numbers[2]

        range_map = {
            "src_start": src_start,
            "src_stop": src_start + length,
            "dst_start": dst_start,
            "length": length,
        }

        self.conversion_map.append(range_map)

    def convert(self, source: int) -> int:
        for m in self.conversion_map:
            if m["src_start"] <= source <= m["src_stop"]:
                return m["dst_start"] + source - m["src_start"]
        return source


def parse_seeds(lines: list[str]) -> list[int]:
    seeds = lines[0].split(" ")
    return [int(s) for s in seeds[1:]]


def parse_name(line: str) -> str:
    return line[: line.find(" map:")]


def get_equivalences(lines: list[str]) -> list[Equivalence]:
    equivalences: list[Equivalence] = []
    current_equivalence = Equivalence(parse_name(lines[2]))
    equivalences.append(current_equivalence)
    for line in lines[3:]:
        if not line:
            continue
        elif " map:" in line:
            current_equivalence = Equivalence(parse_name(line))
            equivalences.append(current_equivalence)
        elif line[0].isdigit():
            current_equivalence.append_to_map(line)

    return equivalences


def apply_equivalences(seed: int, equivalences: list[Equivalence]) -> int:
    result = seed
    for equivalence in equivalences:
        result = equivalence.convert(result)
    return result


def compute_locations(lines: list[str]) -> list[int]:
    seeds: list[int] = parse_seeds(lines)
    equivalences: list[Equivalence] = get_equivalences(lines)
    locations: list[int] = []

    for seed in seeds:
        locations.append(apply_equivalences(seed, equivalences))

    return locations


def get_lowest_location(lines: list[str]) -> int:
    return sorted(compute_locations(lines))[0]


if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()
    print(f"Part I - Lowest location is {get_lowest_location(lines)}.")
