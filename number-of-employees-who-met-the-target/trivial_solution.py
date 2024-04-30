from typing import List


def numberOfEmployeesWhoMetTarget(hours: List[int], target: int) -> int:
    counter = 0
    for hour in hours:
        if hour >= target:
            counter += 1
    return counter


if __name__ == '__main__':
    hours, target = [0, 1, 2, 3, 4], 2
    result = numberOfEmployeesWhoMetTarget(hours, target)
    print(result)
