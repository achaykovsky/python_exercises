from typing import List

#Time Complexity: O(n^2)
#Space Complexity: O(1)
def pivotIndex(nums: List[int]) -> int:
    nums = [0] + nums + [0]

    for i in range(1, len(nums) - 1):
        left = sum(nums[:i])
        right = sum(nums[i + 1: len(nums)])
        if left == right:
            return i - 1

    return -1


if __name__ == '__main__':
    nums = [2,1,-1]
    result = pivotIndex(nums)
    print(result)
