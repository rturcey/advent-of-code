from dataclasses import dataclass


@dataclass
class Race:
    duration: int
    record_distance: int


def parse_races(lines: list[str], part2=False) -> list[Race]:
    if part2:
        durations = [int(lines[0].split(":")[1].replace(" ", ""))]
        record_distances = [int(lines[1].split(":")[1].replace(" ", ""))]
    else:
        durations = [int(d) for d in lines[0].split(":")[1].split(" ") if d]
        record_distances = [int(r) for r in lines[1].split(":")[1].split(" ") if r]

    races: list[Race] = []

    for i in range(0, len(durations)):
        races.append(Race(durations[i], record_distances[i]))

    return races


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
