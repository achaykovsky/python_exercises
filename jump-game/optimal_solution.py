from typing import List


# Optimal solution for the Jump Game problem using a greedy approach.

# Time Complexity: O(n)
# Space Complexity:O(1)
def canJump(nums: List[int]) -> bool:
    goal = 0

    # Traverse the array from the end to the beginning to find the last index we can reach
    for i in range(len(nums) - 1, -1, -1):
        # If the current index can reach the goal, update the goal to this index
        if i + nums[i] >= goal:
            goal = i

    return goal == 0


if __name__ == '__main__':
    nums = [3, 2, 1, 0, 4]  # False
    nums = [2, 3, 1, 1, 4]  # True
    result = canJump(nums)
    print(result)
