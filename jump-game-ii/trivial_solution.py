from typing import List
from collections import deque


# BFS Approach


# Time Complexity: O(n^2)
# Space Complexity: O(n)
def jump(nums: List[int]) -> int:
    n = len(nums)
    queue = deque([0])
    visited = [False] * n
    visited[0] = True  # start from the first position
    counter = 0
    result = len(nums)

    while queue:
        size = len(queue)

        for _ in range(size):  # for each level of the BFS
            current = queue.popleft()

            if current >= n - 1:  # if we reach the last index
                result = min(result, counter)
                return result

            for step in range(1, nums[current] + 1):
                next_pos = current + step

                if next_pos < n and not visited[next_pos]:
                    visited[next_pos] = True
                    queue.append(next_pos)

        counter += 1

    return result


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    result = jump(nums)
    print(result)
