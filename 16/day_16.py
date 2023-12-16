from dataclasses import dataclass

# . / \ | -
EMPTY = 0
MIRROR_RIGHT = 1
MIRROR_LEFT = 2
VERT_SPLITTER = 3
HORIZ_SPLITTER = 4

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3


@dataclass
class Point:
    x: int
    y: int
    type: int
    energized: bool
    energized_from: tuple[int, int] | None

    def coordinates(self) -> tuple[int, int]:
        return self.x, self.y

    def __str__(self):
        return f"({self.x},{self.y}) {self.type} {self.energized}"

    def __char__(self):
        if self.energized:
            return "#"
        return "."


@dataclass
class Beam:
    current_point: Point
    direction: int


def get_type(c: str) -> int:
    if c == ".":
        return EMPTY
    if c == "/":
        return MIRROR_RIGHT
    if c == "L":
        return MIRROR_LEFT
    if c == "|":
        return VERT_SPLITTER
    if c == "-":
        return HORIZ_SPLITTER


def parse_lines(lines: list[str]) -> list[Point]:
    points: list[Point] = []
    for y, line in enumerate(lines):
        line = line.replace("\\", "L")
        for x, c in enumerate(line):
            points.append(Point(x, y, get_type(c), False, None))
    return points


def get_point(x: int, y: int, points: list[Point]) -> Point | None:
    for p in points:
        if p.coordinates() == (x, y):
            return p
    return None


def compute_direction(p: Point, d: int) -> int:
    if (
        (p.type == EMPTY and d == UP)
        or (p.type == VERT_SPLITTER and d == UP)
        or (p.type == MIRROR_RIGHT and d == RIGHT)
        or (p.type == MIRROR_LEFT and d == LEFT)
    ):
        return UP

    if (
        (p.type == EMPTY and d == DOWN)
        or (p.type == VERT_SPLITTER and d == DOWN)
        or (p.type == MIRROR_RIGHT and d == LEFT)
        or (p.type == MIRROR_LEFT and d == RIGHT)
    ):
        return DOWN

    if (
        (p.type == EMPTY and d == RIGHT)
        or (p.type == HORIZ_SPLITTER and d == RIGHT)
        or (p.type == MIRROR_RIGHT and d == UP)
        or (p.type == MIRROR_LEFT and d == DOWN)
    ):
        return RIGHT

    return LEFT


def move(origine: Point, direction: int, points: list[Point]) -> Point | None:
    if direction == UP:
        return get_point(origine.x, origine.y - 1, points)
    if direction == DOWN:
        return get_point(origine.x, origine.y + 1, points)
    if direction == RIGHT:
        return get_point(origine.x + 1, origine.y, points)
    if direction == LEFT:
        return get_point(origine.x - 1, origine.y, points)


def duplicate_beam(p: Point, d: int) -> tuple[bool, int, int]:
    if p.type == HORIZ_SPLITTER:
        if d in [UP, DOWN]:
            return True, LEFT, RIGHT
    elif p.type == VERT_SPLITTER:
        if d in [LEFT, RIGHT]:
            return True, UP, DOWN
    return False, -1, -1


def move_beams(points: list[Point], starting_beam: Beam):
    beams = [starting_beam]
    beams_queue = []
    while beams:
        for i, b in enumerate(beams):
            while True:
                b.current_point.energized = True
                should_duplicate, d1, d2 = duplicate_beam(b.current_point, b.direction)
                if should_duplicate:
                    b.direction = d1
                    beams_queue.append(Beam(b.current_point, d2))
                b.direction = compute_direction(b.current_point, b.direction)
                old_point = b.current_point
                point = move(b.current_point, b.direction, points)
                if not point or (
                    point.energized and point.energized_from == old_point.coordinates()
                ):
                    beams = [] if len(beams) == 1 else beams[:i] + beams[i + 1 :]
                    break
                else:
                    b.current_point = point
                    b.current_point.energized_from = old_point.coordinates()
        if not beams:
            beams = beams_queue
            beams_queue = []


def points_to_lines(points: list[Point]) -> list[str]:
    lines: list[str] = []
    for p in sorted(points, key=lambda p: (p.y, p.x)):
        if p.y >= len(lines):
            lines.append("")
        lines[p.y] += p.__char__()
    print("\n".join(lines))
    return lines


def sum_tiles(lines: list[str], part2=False) -> int:
    beams: list[Beam] = []
    counts: list[int] = []

    if part2:
        for i in range(len(lines[0])):
            beams.append(Beam(Point(i, -1, EMPTY, False, None), DOWN))
            beams.append(Beam(Point(i, len(lines), EMPTY, False, None), UP))
        for i in range(len(lines)):
            beams.append(Beam(Point(-1, i, EMPTY, False, None), RIGHT))
            beams.append(Beam(Point(len(lines[0]), i, EMPTY, False, None), LEFT))
    else:
        beams.append(Beam(Point(-1, 0, EMPTY, False, None), RIGHT))

    for b in beams:
        points = parse_lines(lines)
        move_beams(points, b)
        counts.append(sum(1 for p in points if p.energized))

    # points_to_lines(points)
    return sorted(counts)[-1]


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
        print(f"Part I - Result: {sum_tiles(lines)}.")
        print(f"Part II - Result: {sum_tiles(lines, True)}.")
