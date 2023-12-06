from dataclasses import dataclass


@dataclass
class Race:
    duration: int
    record_distance: int


def parse_races(lines: list[str], part2=False) -> list[Race]:
    numbers_list: list[list[int]] = []
    for line in lines:
        numbers = line.split(":")[1]
        if part2:
            numbers = numbers.replace(" ", "")
        numbers_list.append([int(n) for n in numbers.split(" ") if n])

    return [Race(i, j) for i, j in zip(*numbers_list)]


def winning_race(hold: int, race: Race) -> bool:
    return hold * (race.duration - hold) > race.record_distance


def sum_winning_races(lines: list[str], part2=False) -> int:
    races: list[Race] = parse_races(lines, part2)
    global_count = 1

    for race in races:
        global_count *= sum(
            1 for h in range(0, race.duration + 1) if winning_race(h, race)
        )

    return global_count


if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()
    file.close()

    print(f"Part I - result: {sum_winning_races(lines)}.")
    print(f"Part II - result: {sum_winning_races(lines, True)}.")
