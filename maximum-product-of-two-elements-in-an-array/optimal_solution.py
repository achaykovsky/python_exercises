from typing import List


def maxProduct(nums: List[int]) -> int:
    first_max = max(nums)
    nums.remove(first_max)
    second_max = max(nums)
    return (first_max - 1) * (second_max - 1)


if __name__ == '__main__':
    nums = [3, 4, 5, 2]
    result = maxProduct(nums)
    print(result)