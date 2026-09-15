from collections import deque
from typing import List


# Inplace solution for counting the number of islands in a grid.

# Time Complexity: O(m*n)
# Space Complexity: O(m*n) - due to the queue used in BFS
def numIslands(grid: List[List[str]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    counter = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(r: int, c: int) -> None:
        queue = deque([(r, c)])
        grid[r][c] = "-1"  # Mark the current cell as visited

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    grid[nr][nc] = "-1"  # Mark the neighbor as visited
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":  # Found an unvisited land
                counter += 1
                bfs(r, c)  # Perform BFS to mark all connected lands

    return counter


if __name__ == '__main__':
    grid = [["1", "1", "1", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "1"]]
    result = numIslands(grid)
    print(result)
