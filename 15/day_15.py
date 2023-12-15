from dataclasses import dataclass


@dataclass
class Lens:
    label: str
    focal_length: int

    def __str__(self):
        return f"[{self.label} {self.focal_length}]"


class Box:
    lenses: list[Lens]
    number: int

    def __init__(self, number: int):
        self.number = number
        self.lenses = []

    def remove_lens(self, name: str):
        for i, l in enumerate(self.lenses):
            if l.label == name:
                self.lenses = self.lenses[:i] + self.lenses[i + 1 :]
                return

    def add_lens(self, name: str, focal_length: int):
        for i, l in enumerate(self.lenses):
            if l.label == name:
                self.lenses[i].focal_length = focal_length
                return
        self.lenses.append(Lens(name, focal_length))

    def __str__(self):
        lenses = [l.__str__() for l in self.lenses]
        return f"Box {self.number}: {' '.join(lenses)}"


def run_hash(sequence: str) -> int:
    current_value = 0
    for c in sequence:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


def sum_hashes(line: str) -> int:
    sequences = line.split(",")
    return sum(run_hash(s) for s in sequences)


def compute_focusing_power(box: Box) -> int:
    count = 0
    for i in range(len(box.lenses)):
        count += (box.number + 1) * (i + 1) * box.lenses[i].focal_length

    return count


def perform_sequence(sequence: str, boxes: list[Box]):
    if "-" in sequence:
        label = sequence[:-1]
        box_number = run_hash(label)
        boxes[box_number].remove_lens(label)
    elif "=" in sequence:
        label, focal_length = sequence.split("=")
        box_number = run_hash(label)
        boxes[box_number].add_lens(label, int(focal_length))


def sum_focusing_power(line: str) -> int:
    sequences = line.split(",")
    boxes = [Box(i) for i in range(256)]
    for s in sequences:
        perform_sequence(s, boxes)
    return sum(compute_focusing_power(b) for b in boxes)


if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.read()
        print(f"Part I - Result: {sum_hashes(line)}.")
        print(f"Part II - Result: {sum_focusing_power(line)}.")
