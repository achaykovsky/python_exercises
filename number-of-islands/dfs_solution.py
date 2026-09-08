from collections import deque
from typing import List


# DFS solution for counting the number of islands in a grid.

# Time Complexity: O(m*n)
# Space Complexity:O(m*n)
def numIslands(grid: List[List[str]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    counter = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "-1"  # Mark the current cell as visited
        for dr, dc in directions:
            dfs(r + dr, c + dc)  # Visit all connected lands

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":  # Found an unvisited land
                counter += 1
                dfs(r, c)  # Perform DFS to mark all connected lands

    return counter


if __name__ == '__main__':
    grid = [["1", "1", "1", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "1"]]
    result = numIslands(grid)
    print(result)
