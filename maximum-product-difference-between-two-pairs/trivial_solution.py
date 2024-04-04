from typing import List


def maxProductDifference(nums: List[int]) -> int:
    nums.sort()
    return (nums[-1] * nums[-2]) - (nums[0] * nums[1])


if __name__ == '__main__':
    nums = [5, 6, 2, 7, 4]
    result = maxProductDifference(nums)
    print(result)
