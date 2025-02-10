from typing import List


# Time Complexity: O(n^3)
# Space Complexity: O(n)
def maxSubArray(nums: List[int]) -> int:
    max_sum = float("-inf")
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            temp_sum = sum(nums[i:j + 1])
            max_sum = max(temp_sum, max_sum)
    return max_sum


if __name__ == '__main__':
    nums = [-1]
    result = maxSubArray(nums)
    print(result)
