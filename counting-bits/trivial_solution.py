from typing import List


def countBits(n: int) -> List[int]:
    result = []

    for i in range(n + 1):
        num = i
        counter = calculate_ones_in_num(num)
        result.append(counter)
    return result


def calculate_ones_in_num(num):
    counter = 0
    while num > 0:
        if num % 2 == 1:
            counter += 1
        num //= 2
    return counter


if __name__ == '__main__':
    n = 2
    result = countBits(n)
    print(result)
