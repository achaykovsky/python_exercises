
from collections import Counter
from typing import List


def findPairs(nums: List[int], k: int) -> int:
    result = 0

    counter = Counter(nums)

    for key, value in counter.items():
        if k == 0:
            if value > 1:
                result += 1
        else:
            if key - k in counter:
                result += 1

    return result


if __name__ == '__main__':
    nums = [1, 3, 1, 5, 4]
    k = 0
    result = findPairs(nums, k)
    print(result)
