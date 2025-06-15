
from typing import List


# Time Complexity: O(nlogn)
# Space Complexity: O(1)
def missingNumber(nums: List[int]) -> int:
    nums.sort()

    for i in range(len(nums)):
        if nums[i] != i:
            return i

    return len(nums)


if __name__ == '__main__':
    nums = [3, 0, 1]
    result = missingNumber(nums)
    print(result)
