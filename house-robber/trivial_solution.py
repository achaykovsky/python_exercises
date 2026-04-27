from typing import List


# This is a recursive solution to the House Robber problem.
# The idea is to use recursion to explore two options at each house (rob or skip current house).

# Time Complexity: O(2^n)
# Space Complexity: O(n)
def rob(nums: List[int]) -> int:
    def dfs_rob(i: int) -> int:
        # Base case: no houses left to rob
        if i >= len(nums):
            return 0

        # Option 1: Rob current house and skip next
        rob_current = nums[i] + dfs_rob(i + 2)

        # Option 2: Skip current house
        skip_current = dfs_rob(i + 1)

        return max(rob_current, skip_current)

    return dfs_rob(0)


if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]
    result = rob(nums)
    print(result)
