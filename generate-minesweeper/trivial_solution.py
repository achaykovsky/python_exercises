import random
from typing import List


# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
def generate_minesweeper(rows: int, cols: int, mines: int) -> List[List[str]]:
    if mines >= rows * cols:
        raise ValueError("Number of mines must be less than total number of cells.")

    board = [["0" for _ in range(cols)] for _ in range(rows)]
    positions = [(r, c) for r in range(rows) for c in range(cols)]
    mine_positions = random.sample(positions, mines)

    for r, c in mine_positions:
        board[r][c] = "*"

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    for r, c in mine_positions:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "*":
                board[nr][nc] = str(int(board[nr][nc]) + 1)

    return board


if __name__ == '__main__':
    rows = 4
    cols = 4
    mines = 3
    result = generate_minesweeper(rows, cols, mines)
    print(result)
