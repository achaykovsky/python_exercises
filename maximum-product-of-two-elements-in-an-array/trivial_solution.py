from typing import List


def maxProduct(nums: List[int]) -> int:
    nums.sort()
    return (nums[-1] - 1) * (nums[-2] - 1)


if __name__ == '__main__':
    nums = [3, 4, 5, 2]
    result = maxProduct(nums)
    print(result)
