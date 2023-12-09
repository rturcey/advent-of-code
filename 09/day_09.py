class Sequence:
    def __init__(self, sequence: str):
        first_sequence = [int(n) for n in sequence.split(" ") if n]
        self.sequences: list[list[int]] = [first_sequence]
        self.compute_subsequences()

    def compute_subsequences(self):
        while not all(n == 0 for n in self.sequences[-1]):
            last_s = self.sequences[-1]
            sub_s = [last_s[i + 1] - last_s[i] for i in range(len(last_s) - 1)]
            self.sequences.append(sub_s)

    def increment_sequences(self):
        for i in range(len(self.sequences) - 1, 0, -1):
            to_append = self.sequences[i - 1][-1] + self.sequences[i][-1]
            self.sequences[i - 1].append(to_append)

    def increment_sequences_backward(self):
        for i in range(len(self.sequences) - 1, 0, -1):
            to_insert = self.sequences[i - 1][0] - self.sequences[i][0]
            self.sequences[i - 1].insert(0, to_insert)


def sum_last_of_first_sequences(lines: list[str]) -> int:
    sequences = [Sequence(line) for line in lines]
    for s in sequences:
        s.increment_sequences()
    return sum(s.sequences[0][-1] for s in sequences)


def sum_first_of_first_sequences(lines: list[str]) -> int:
    sequences = [Sequence(line) for line in lines]
    for s in sequences:
        s.increment_sequences_backward()
    return sum(s.sequences[0][0] for s in sequences)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
        result = sum_last_of_first_sequences(lines)
        print(f"Part I - Result: {result}.")
        result = sum_first_of_first_sequences(lines)
        print(f"Part II - Result: {result}.")
