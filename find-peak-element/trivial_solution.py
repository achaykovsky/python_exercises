from typing import List


# Optimal solution using Binary Search

# In this problem,it won't matter if we're biased to the left or to the right-> it will affect on which peak we find
# Here we are biased to the left


# Time Complexity: O(logn)
# Space Complexity: O(1)
def findPeakElement(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # We check the right side of the peak (mid, mid+1)
        if nums[mid] > nums[mid + 1]:
            # We're on the descending slope.
            # The peak is either at mid or somewhere to the left of it
            right = mid
        else:
            # We're on the ascending slope.
            # This means a peak must exist to the right of mid (not including mid)
            left = mid + 1

    # we're effectively eliminating one side of the slope and narrowing toward the peak.
    return left  # returning the index


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    result = findPeakElement(nums)
    print(result)
