from typing import List


# Time Complexity: O(n)
# Space Complexity: O(n)
def pivotIndex(nums: List[int]) -> int:
    nums = [0] + nums + [0]  # creates a new list -> space O(n)
    total_sum = sum(nums)
    left, l = 0, 0

    for r in range(1, len(nums) - 1):
        left += nums[l]  # running sum
        right = total_sum - left - nums[r]  # calculating the right side, but ignoring the pivot value(nums[r])
        if left == right:
            return r - 1  # we shifted the indices by the zero padding
        l += 1
    return -1


if __name__ == '__main__':
    nums = [2, 1, -1]
    result = pivotIndex(nums)
    print(result)
