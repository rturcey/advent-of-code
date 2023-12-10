import sys
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def tuple(self) -> tuple[int, int]:
        return self.x, self.y


def replace_char(grid: list[str], y: int, x: int, new: str):
    grid[y] = grid[y][:x] + new + grid[y][x+1:]


def move(grid: list[str], p: Point, prev: Point, count: int) -> int:

    if p.y >= len(grid) or p.y < 0:
        return -1
    if p.x < 0 or p.x >= len(grid[p.y]):
        return -1

    replace_char(grid, prev.y, prev.x, "*")

    match grid[p.y][p.x]:
        case "S":
            return count
        case "|":
            if prev.y > p.y:
                return move(grid, Point(p.x, p.y-1), p, count+1)
            elif prev.y < p.y:
                return move(grid, Point(p.x, p.y+1), p, count+1)
        case "-":
            if prev.x > p.x:
                return move(grid, Point(p.x-1, p.y), p, count+1)
            elif prev.x < p.x:
                return move(grid, Point(p.x+1, p.y), p, count+1)
        case "L":
            if prev.x > p.x:
                return move(grid, Point(p.x, p.y-1), p, count+1)
            elif prev.y < p.y:
                return move(grid, Point(p.x+1, p.y), p, count+1)
        case "J":
            if prev.y < p.y:
                return move(grid, Point(p.x-1, p.y), p, count+1)
            elif prev.x < p.x:
                return move(grid, Point(p.x, p.y-1), p, count+1)
        case "7":
            if prev.x < p.x:
                return move(grid, Point(p.x, p.y+1), p, count+1)
            if prev.y > p.y:
                return move(grid, Point(p.x-1, p.y), p, count+1)
        case "F":
            if prev.x > p.x:
                return move(grid, Point(p.x, p.y+1), p, count+1)
            if prev.y > p.y:
                return move(grid, Point(p.x+1, p.y), p, count+1)
    return -1


def find_loop(lines: list[str]) -> int:
    sys.setrecursionlimit(500000)
    s_pos: Point = Point(0,0)
    for y in range(len(lines)):
        if "S" in lines[y]:
            s_pos = Point(lines[y].find("S"), y)
            break

    count = move(lines, Point(s_pos.x+1, s_pos.y), s_pos, 1)
    if count < 0:
        count = move(lines, Point(s_pos.x-1, s_pos.y), s_pos, 1)
        if count < 0:
            count = move(lines, Point(s_pos.x, s_pos.y+1), s_pos, 1)

    count = 0
    for l in lines:
        count += l.count("*")

    return int(count / 2)



if __name__ == '__main__':
    with open("input.txt") as f:
        sys.setrecursionlimit(5000)
        lines = f.readlines()
        print(f"Part I - Result: {find_loop(lines)}.")