from typing import List


def buildArray(nums: List[int]) -> List[int]:
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = [nums[i] for i in nums]
    return res


if __name__ == '__main__':
    nums = [0, 2, 1, 5, 3, 4]
    result = buildArray(nums)
    print(result)
