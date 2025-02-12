from typing import List


# Exponent: Maximum Subarray Sum

# Time Complexity: O(n)
# Space Complexity: O(1)

# Kadane’s Algorithm
def maxSubArray(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    max_sum = nums[0]
    curr_running_sum = 0

    for num in nums:
        # summing positive running sum
        curr_running_sum += num
        max_sum = max(curr_running_sum, max_sum)

        # resetting negative running sum to zero
        if curr_running_sum < 0:
            curr_running_sum = 0

    return max_sum


if __name__ == '__main__':
    nums = [-1, 2, -3, 4]
    result = maxSubArray(nums)
    print(result)
