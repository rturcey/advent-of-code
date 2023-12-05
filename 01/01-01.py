import sys


def compute_calibration_sum(file_name: str) -> int:
    file = open(file_name, "r")
    calibration_sum = 0

    for line in file.readlines():
        numbers = [int(c) for c in line if c.isdigit()]
        calibration_sum += numbers[0] * 10 + numbers[-1]

    return calibration_sum


if __name__ == '__main__':
    print(compute_calibration_sum(sys.argv[1]))
