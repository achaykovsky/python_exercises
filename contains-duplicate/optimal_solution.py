from typing import List


# The advantage of this solution is that we can stop before looping through all the items.

# Time Complexity: O(n)
# Space Complexity: O(n)
def solution(nums: List[int]) -> bool:
    visited_numbers = set()
    for num in nums:
        if num in visited_numbers:
            return True
        visited_numbers.add(num)
    return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    result = solution(nums)
    print(result)
