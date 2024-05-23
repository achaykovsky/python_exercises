# This is a generic file for the trivial solution
from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    result = -1

    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return result


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 1000
    result = search(nums, target)
    print(result)
