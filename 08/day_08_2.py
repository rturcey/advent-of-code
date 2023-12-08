import math
import re
import threading


def parse_instructions(line: str) -> list[int]:
    instructions: list[int] = []
    for i in line:
        if i == "L":
            instructions.append(0)
        elif i == "R":
            instructions.append(1)
    return instructions


def parse_lines(lines: list[str]) -> tuple[list[int], dict]:
    instructions = parse_instructions(lines[0])
    networks: dict = {}
    pattern = r"([A-Z\d]{3})"

    for line in lines[2:]:
        matches = re.findall(pattern, line)
        networks[matches[0]] = [matches[1], matches[2]]

    return instructions, networks


def get_first_count(instructions: list[int], networks: dict, key: list) -> int:
    count = 0

    while True:
        i = 0
        while i < len(instructions):
            key = networks[key][instructions[i]]
            count += 1
            if key.endswith("Z"):
                return count
            i += 1


def count_all_z(lines: list[str]) -> int:
    instructions, networks = parse_lines(lines)
    first_matches = [
        get_first_count(instructions, networks, k)
        for k in networks.keys()
        if k.endswith("A")
    ]

    return math.lcm(*first_matches)


if __name__ == "__main__":
    with open("input.txt") as f:
        print(f"Part II - Result: {count_all_z(f.readlines())}.")
