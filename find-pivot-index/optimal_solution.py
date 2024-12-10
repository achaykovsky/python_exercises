from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)
def pivotIndex(nums: List[int]) -> int:
    total_sum = sum(nums)
    left = 0

    for r in range(len(nums)):
        right = total_sum - left - nums[r]  # calculating the right side, but ignoring the pivot value(nums[r])
        if left == right:
            return r  # we shifted the indices by the zero padding
        left += nums[r]
    return -1


if __name__ == '__main__':
    nums = [2, 1, -1]
    result = pivotIndex(nums)
    print(result)
