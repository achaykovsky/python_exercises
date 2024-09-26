from collections import Counter
from typing import List


def countKDifference(nums: List[int], k: int) -> int:
    result = 0
    freq_nums = Counter(nums)

    length = len(freq_nums) - 1
    for i in range(1, length):
        if i + k <= length:
            result += freq_nums[i] * freq_nums[i + k]
    return result


if __name__ == '__main__':
    # nums = [3, 2, 1, 5, 4]
    # k = 2

    # nums = [1, 2, 2, 1]
    # k = 1

    nums = [1, 3]
    k = 3
    result = countKDifference(nums, k)
    print(result)
