from typing import List


# Time Complexity: O(2^n)
# Space Complexity: O(n)
def canJump(nums: List[int]) -> bool:
    def backtrack(position: int) -> bool:
        if position >= len(nums) - 1:  # Base case: if we reach the last index
            return True
        max_jump = nums[position]  # Maximum jump from the current position
        for step in range(1, max_jump + 1):
            if backtrack(position + step):  # Recursive call to check if we can reach the end from the next position
                return True
        return False

    return backtrack(0)


if __name__ == '__main__':
    nums = [3, 2, 1, 0, 4]
    nums = [2, 3, 1, 1, 4]
    result = canJump(nums)
    print(result)
