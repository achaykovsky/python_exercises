from typing import List


# Time Complexity: O(n)
# Space Complexity:O(1)
def canJump(nums: List[int]) -> bool:
    max_reach = 0

    for curr_pos, jump_step in enumerate(nums):
        # If the current index is beyond the maximum reachable index, we cannot proceed
        if curr_pos > max_reach:
            return False

        # Update the maximum reachable index
        max_reach = max(max_reach, curr_pos + jump_step)

    return True


if __name__ == '__main__':
    nums = [3, 2, 1, 0, 4]  # False
    nums = [2, 3, 1, 1, 4]  # True
    result = canJump(nums)
    print(result)
