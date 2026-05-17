from typing import List


# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
def hasPath(maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    rows = len(maze)
    cols = len(maze[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()

    def dfs(r: int, c: int) -> bool:
        # No Further need to explore this path
        if (r, c) in visited:
            return False

        if [r, c] == destination:
            return True

        visited.add((r, c))

        for dr, dc in directions:
            row, col = r, c

            # The ball is rolling in the (dr,dc) direction inside the borders
            while (0 <= row + dr < rows and
                   0 <= col + dc < cols and
                   maze[row + dr][col + dc] == 0):
                row += dr
                col += dc

            # The ball hit the wall and stopped
            # Starts looking for a new path from (row,col)
            if dfs(row, col):
                return True

        # No path has been found from this route
        return False

    return dfs(start[0], start[1])


if __name__ == '__main__':
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    start = [0, 4]
    destination = [4, 4]
    result = hasPath(maze, start, destination)
    print(result)
