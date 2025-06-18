from typing import List


# The idea is to use XOR's self-canceling property to isolate the missing number

# Time Complexity: O(n)
# Space Complexity: O(1)
def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    missing = n
    for i in range(n):
        missing ^= i ^ nums[i]  # XORing all the numbers that should be present with the numbers that are present

    return missing


if __name__ == '__main__':
    nums = [3, 0, 1]
    result = missingNumber(nums)
    print(result)
