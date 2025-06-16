from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)
def missingNumber(nums: List[int]) -> int:
    nums_sum = sum(nums)  # O(n)
    n = len(nums)
    expected_sum = n * (n + 1) // 2

    return expected_sum - nums_sum


if __name__ == '__main__':
    nums = [3, 0, 1]
    result = missingNumber(nums)
    print(result)
