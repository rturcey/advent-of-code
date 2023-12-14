def parse_lines(lines: list[str]) -> list[list[str]]:
    patterns: list[list[str]] = [[]]
    for l in lines:
        if not l:
            patterns.append([])
        else:
            patterns[-1].append(l)
    return patterns


def col_to_rows(pattern: list[str]) -> list[str]:
    rows: list[str] = []
    for i in range(len(pattern[0])):
        new_str = "".join([pattern[j][i] for j in range(len(pattern))])
        rows.append(new_str)
    return rows


def opposite(pattern: list[str], y: int, x: int):
    c = "." if pattern[y][x] == "#" else "#"
    pattern[y] = pattern[y][:x] + c + pattern[y][x + 1 :]


def find_mirror(
    pattern: list[str],
    is_column: bool,
    old_mirror: tuple,
    mirror_indexes: [],
    part2=False,
) -> int:
    changed = False
    origin_pattern = ["" + s for s in pattern]
    for i in range(len(pattern) - 1):
        diff = []
        if part2 and not changed:
            for j, c in enumerate(pattern[i]):
                if len(diff) > 1:
                    break
                if c != pattern[i + 1][j]:
                    diff.append(j)
        if part2 and len(diff) == 1 and not changed:
            opposite(pattern, i, diff[0])
            changed = True

        if pattern[i] == pattern[i + 1] and (
            not part2
            or (
                old_mirror[0] != i
                or (old_mirror[0] == i and old_mirror[1] != is_column)
            )
        ):
            start = i
            end = i + 1
            while start >= 0 and end < len(pattern):
                if pattern[start] != pattern[end]:
                    if changed:
                        pattern = origin_pattern
                        changed = False
                    diff = []
                    if part2 and not changed:
                        for j, c in enumerate(pattern[start]):
                            if len(diff) > 1:
                                break
                            if c != pattern[end][j]:
                                diff.append(j)
                    if part2 and len(diff) == 1 and not changed:
                        opposite(pattern, start, diff[0])
                        changed = True
                    else:
                        break
                start -= 1
                end += 1
                if start == -1 or end == len(pattern):
                    if not part2:
                        mirror_indexes.append((i, is_column))
                    return i + 1
    return -1


def sum_repeated(
    lines: list[str], mirror_indexes: list, part2=False
) -> tuple[int, list[int]]:
    patterns = parse_lines(lines)
    count = 0
    for i, pattern in enumerate(patterns):
        col = find_mirror(
            col_to_rows(pattern),
            True,
            () if not part2 else mirror_indexes[i],
            mirror_indexes,
            part2,
        )
        if col > -1:
            count += col
        row = find_mirror(
            pattern,
            False,
            () if not part2 else mirror_indexes[i],
            mirror_indexes,
            part2,
        )
        if row > -1:
            count += row * 100
    return count, mirror_indexes


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
        res, indexes = sum_repeated(lines, [])
        print(f"Part I - Result: {res}.")
        res, indexes = sum_repeated(lines, indexes, True)
        print(f"Part II - Result: {res}.")
