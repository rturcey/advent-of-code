from dataclasses import dataclass


@dataclass
class Galaxy:
    x: int
    y: int
    number: int

    def __str__(self):
        return f"{self.number}: {self.x},{self.y}"


def add_column(lines: list[str], pos: int):
    for i, line in enumerate(lines):
        lines[i] = line[:pos] + "." + line[pos:]


def empty_column(lines: list[str], pos: int) -> bool:
    return not any(e != "." for e in [l[pos] for l in lines])


def empty_line(line: str) -> bool:
    return not any(e != "." for e in line)


def get_indexes_to_expand(lines: list[str]) -> dict:
    lines_to_add: list[int] = []
    for i, line in enumerate(lines):
        if empty_line(line):
            lines_to_add.append(i)

    columns_to_add: list[int] = []
    for i, column in enumerate(lines[0]):
        if empty_column(lines, i):
            columns_to_add.append(i)

    return {"rows": lines_to_add, "columns": columns_to_add}


def get_galaxies(lines: list[str], expanded: dict, expansion_size: int) -> list[Galaxy]:
    galaxies: list[Galaxy] = []
    galaxy_number = 1

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "#":
                true_x = x + sum(
                    expansion_size - 1 for r in expanded["columns"] if r < x
                )
                true_y = y + sum(expansion_size - 1 for r in expanded["rows"] if r < y)
                galaxies.append(Galaxy(true_x, true_y, galaxy_number))
                galaxy_number += 1

    return galaxies


def compute_shortest_path(g1: Galaxy, g2: Galaxy) -> int:
    sh = abs(g1.y - g2.y) + abs(g1.x - g2.x)
    return sh


def get_shortest_paths_sum(lines: list[str], expansion_size: int) -> int:
    expanded = get_indexes_to_expand(lines)
    galaxies = get_galaxies(lines, expanded, expansion_size)
    s_paths_sum = 0

    for g1 in galaxies:
        to_add = sum(
            compute_shortest_path(g1, g2)
            for g2 in [g for g in galaxies if g.number > g1.number]
        )
        s_paths_sum += to_add

    return s_paths_sum


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
        print(f"Part I - Result: {get_shortest_paths_sum(lines, 2)}.")
        print(f"Part I - Result: {get_shortest_paths_sum(lines, 1000000)}.")
