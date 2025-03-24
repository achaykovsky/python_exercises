from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)

def findMaxAverage(nums: List[int], k: int) -> float:
    windows_sum = sum(nums[:k])  # initializing the sliding window
    max_sum = windows_sum

    for i in range(k, len(nums)):
        windows_sum += nums[i] - nums[i - k]  # adding the new element, and removing the last one
        max_sum = max(max_sum, windows_sum)

    return max_sum / k


if __name__ == '__main__':
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    result = findMaxAverage(nums, k)
    print(result)
