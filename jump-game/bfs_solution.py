from typing import List


# Time Complexity: O(n^2)
# Space Complexity: O(n)
def canJump(nums: List[int]) -> bool:
    n = len(nums)
    visited = [False] * n
    queue = [0]

    while queue:
        current = queue.pop(0)
        if current >= n - 1:  # Base case: if we reach the last index
            return True
        if visited[current]:
            continue
        visited[current] = True

        for step in range(1, nums[current] + 1):  # Maximum jump from the current position
            next_pos = current + step
            if next_pos < n and not visited[next_pos]:  # Check if we can jump to the next position
                queue.append(next_pos)

    return False


if __name__ == '__main__':
    nums = [3, 2, 1, 0, 4]
    # nums = [2, 3, 1, 1, 4]
    # nums = [1]
    # nums = [1, 2, 3]
    result = canJump(nums)
    print(result)
