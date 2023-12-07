HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE_KIND = 3
FULL_HOUSE = 4
FOUR_KIND = 5
FIVE_KIND = 6


class Hand:
    def __init__(self, cards: list[str], bid: str, part2 = False):
        self.cards: list[str] = cards
        self.bid: int = int(bid)

        self.part2: bool = part2
        self.rank: int = 0
        self.hand_type = self.get_hand_type()

    def get_card_values(self) -> list[int]:
        values: list[int] = []

        for card in self.cards:
            value = 0
            if card.isdigit():
                value = int(card)
            match card:
                case "T":
                    value = 10
                case "J":
                    value = 11 if not self.part2 else 0
                case "Q":
                    value = 12
                case "K":
                    value = 13
                case "A":
                    value = 14
            values.append(value)

        return values

    def get_hand_type(self) -> int:
        s = sorted(self.cards)
        if self.part2:
            s = [c for c in s if c != "J"]

        i = 0
        counts = []
        while i < len(s) - 1:
            if s[i] != s[i + 1]:
                counts.append(0)
            else:
                if not counts:
                    counts.append(0)
                counts[-1] += 1
            i += 1

        if self.part2:
            if not counts:
                counts.append(0)
            counts = sorted(counts, reverse=True)
            counts[0] += self.cards.count("J")

        if 4 in counts or 5 in counts:
            return FIVE_KIND
        if 3 in counts:
            return FOUR_KIND
        if 2 in counts:
            return FULL_HOUSE if 1 in counts else THREE_KIND
        if counts.count(1) == 2:
            return TWO_PAIR
        if 1 in counts:
            return ONE_PAIR
        return HIGH_CARD

    def score(self) -> int:
        return self.bid * self.rank

    def __str__(self):
        return f"cards={self.cards}, bid={self.bid}, type={self.hand_type}, rank={self.rank}"


def sort_hands_key(h: Hand):
    return h.hand_type, h.get_card_values()


def rank_hands(hands: list[Hand]):
    sorted_hands = sorted(hands, key=sort_hands_key)
    for i, hand in enumerate(sorted_hands):
        hand.rank = i + 1

def parse_hands(lines: list[str], part2 = False) -> list[Hand]:
    hands: list[Hand] = []

    for line in lines:
        numbers = line.split(" ")
        hands.append(Hand(*numbers, part2))

    return hands


def sum_scores(lines: list[str], part2 = False):
    hands = parse_hands(lines, part2)
    rank_hands(hands)

    return sum(h.score() for h in hands)


if __name__ == '__main__':
    with open("input.txt") as file:
        lines = file.readlines()
        print(f"Part I - Result: {sum_scores(lines)}.")
        print(f"Part II - Result: {sum_scores(lines, True)}.")