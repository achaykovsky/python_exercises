from typing import List


# Time Complexity: O(m*n)
# Space Complexity: O(n)
def countBattleships(board: List[List[str]]) -> int:
    counter = 0
    rows = len(board)
    cols = len(board[0])
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # 4 possible directions

    def dfs(r, c):
        board[r][c] = '.'

        for dr, dc in directions:  # moving by the direction
            new_r = r + dr
            new_c = c + dc

            # validating boundaries and the current cell is part of a ship
            if 0 <= new_r < rows and 0 <= new_c < cols and board[new_r][new_c] == 'X':
                dfs(new_r, new_c)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'X':
                counter += 1  # found a ship
                dfs(r, c)

    return counter


if __name__ == '__main__':
    board = [["X", ".", ".", "X"],
             [".", ".", ".", "X"],
             [".", ".", ".", "X"]]
    result = countBattleships(board)
    print(result)
