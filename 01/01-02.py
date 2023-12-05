import sys


digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def find_digit(line: str, reverse: bool = False) -> tuple[int, int]:
    index = -1
    digit = 0

    for i in range(0, len(line)):
        if line[i].isdigit():
            index = i
            digit = line[i]
            if not reverse:
                break

    return index, int(digit)


def find_spelled_digit(line: str, reverse: bool = False) -> tuple[int, int]:
    index = -1
    digit = 0
    for spelled in digits.keys():
        digit_index = line.rfind(spelled) if reverse else line.find(spelled)
        if digit_index == -1:
            continue
        if reverse and digit_index > index or (not reverse and (digit_index < index or index == -1)):
            index = digit_index
            digit = digits[spelled]
    return index, digit


def compute_calibration_sum(file_name: str) -> int:
    file = open(file_name, "r")
    calibration_sum = 0

    for line in file.readlines():
        numbers = [
            find_spelled_digit(line),
            find_spelled_digit(line, True),
            find_digit(line),
            find_digit(line, True)
        ]

        numbers = sorted([n for n in numbers if n[0] != -1])
        calibration_sum += numbers[0][1] * 10 + numbers[-1][1]

    return calibration_sum


if __name__ == '__main__':
    print(compute_calibration_sum(sys.argv[1]))
