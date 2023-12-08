import re


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
    pattern = r"([A-Z]{3})"

    for line in lines[2:]:
        matches = re.findall(pattern, line)
        networks[matches[0]] = [matches[1], matches[2]]

    return instructions, networks


def count_steps(lines: list[str]) -> int:
    instructions, networks = parse_lines(lines)

    current_line = "AAA"
    count = 0
    while True:
        for i in instructions:
            current_line = networks[current_line][i]
            count += 1
            if current_line == "ZZZ":
                return count


if __name__ == "__main__":
    with open("input.txt") as f:
        print(f"Part I - Result: {count_steps(f.readlines())}.")
