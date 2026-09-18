from collections import deque
from typing import List


# Time Complexity: O(m*n)
# Space Complexity:O(m*n)
def numIslands(grid: List[List[str]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    counter = 0
    visited = set()
    queue = deque()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(r: int, c: int) -> None:
        # current
        queue.append((r, c))
        visited.add((r, c))  # adding the current to the visited

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited and grid[nr][nc] == "1":
                    visited.add((nr, nc))  # adding the neighbor to the visited
                    queue.append((nr, nc))  # append in order to find check it's neighbors as well

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:  # checking my current cell
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
