# First Missing Positive (Leetcode hard)
# Getting a Different Number (Pramp)

from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)
def missingNumber(nums: List[int]) -> int:
    n = len(nums)

    for i in range(n):
        curr = nums[i]
        while 1 <= curr <= n and curr != nums[curr - 1]:
            swap(nums, i, curr - 1)
            curr = nums[i]  # Update curr to the new value at index i

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


def swap(arr: List[int], a: int, b: int) -> List[int]:
    arr[a], arr[b] = arr[b], arr[a]
    return arr


if __name__ == '__main__':
    nums = [0]
    result = missingNumber(nums)
    print(result)
