# This is a generic file for the trivial solution
from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    maximum = max(candies)
    result = []
    for candy in candies:
        candy += extraCandies
        if candy >= maximum:
            result.append(True)
        else:
            result.append(False)
    return result


if __name__ == '__main__':
    candies = [2, 3, 5, 1, 3]
    result = kidsWithCandies(candies, 3)
    print(result)
