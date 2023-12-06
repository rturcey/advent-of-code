import re
import threading
from dataclasses import dataclass


locations_lock = threading.Lock()


@dataclass
class Range:
    src: int
    dst: int
    range: int

    @property
    def min(self):
        return self.src

    @property
    def max(self):
        return self.src + self.range

    def __str__(self):
        return f"Range({self.min},{self.max})"


class Equivalence:
    def __init__(self, name: str):
        self.name = name
        self.ranges: list[Range] = []

    def append_to_map(self, line: str):
        numbers = [int(n) for n in line.split(" ")]
        src_start, dst_start, length = numbers[0], numbers[1], numbers[2]

        self.ranges.append(Range(src_start, dst_start, length))

    def convert(self, source: int) -> int:
        for r in self.ranges:
            if r.min <= source <= r.max:
                return r.dst + source - r.min
        return source


def sort_ranges(ranges: list[Range]) -> list[Range]:
    return sorted(ranges, key=lambda r: r.min)


def parse_seeds(lines: list[str], part1=False) -> list[Range]:
    numbers = [int(s) for s in lines[0].split(" ")[1:]]
    if part1:
        return [Range(n, n, 1) for n in numbers]

    seeds: list[Range] = []

    i = 0
    while i < len(numbers):
        seeds.append(Range(numbers[i], numbers[i], numbers[i + 1]))
        i += 2

    return sort_ranges(seeds)


def in_seeds(source: int, seeds: list[Range]) -> bool:
    for r in seeds:
        if r.max >= source >= r.min:
            return True
    return False


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


def apply_equivalences(location: int, equivalences: list[Equivalence]) -> int:
    result = location
    for equivalence in equivalences[::-1]:
        result = equivalence.convert(result)
    return result


def get_lowest_location(
    location_start: int,
    location_max: int,
    equivalences: list[Equivalence],
    seeds: list[Range],
    locations: list,
) -> int:

    location = location_start
    while location <= location_max:
        eq = apply_equivalences(location, equivalences)
        if in_seeds(eq, seeds):
            with locations_lock:
                locations.append(location)
            return location
        location += 1

    return -1


if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()
    file.close()

    equivalences = get_equivalences(lines)
    seeds = parse_seeds(lines)

    locations = []
    threads = []
    index = 10000000
    length = 100000

    while index < 20000000:
        thread = threading.Thread(
            target=get_lowest_location,
            args=(
                index,
                index + length,
                equivalences,
                seeds,
                locations,
            ),
        )
        threads.append(thread)
        index += length + 1

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Part II - Lowest location is {sorted(locations)[0]}.")
