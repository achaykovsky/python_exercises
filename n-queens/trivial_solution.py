from typing import List


# Trivial solution for the N-Queens problem
# The N-Queens problem is to place n queens on an n x n chessboard such that no two queens threaten each other.
# This solution uses backtracking to explore all possible placements of queens on the board.

# diagonals are from left to right (row-col)
# anti-diagonals are from right to left (row+col)


# Time Complexity: O(n!)
# Space Complexity: O(n)

def solveNQueens(n: int) -> List[List[str]]:
    result = []
    board = [['.'] * n for _ in range(n)]
    cols = set()
    diagonal = set()  # r - c
    anti_diagonal = set()  # r + c

    def dfs(row: int):
        if row == n:
            result.append([''.join(board[i]) for i in range(n)])
            return

        for col in range(n):
            curr_diagonal = row - col
            curr_anti_diagonal = row + col

            # Check if the column or diagonals are already occupied
            if (col in cols or
                    curr_diagonal in diagonal or
                    curr_anti_diagonal in anti_diagonal):
                continue

            # Place the queen
            board[row][col] = 'Q'
            cols.add(col)
            diagonal.add(curr_diagonal)
            anti_diagonal.add(curr_anti_diagonal)

            dfs(row + 1)

            # Remove the queen
            board[row][col] = '.'
            cols.remove(col)
            diagonal.remove(curr_diagonal)
            anti_diagonal.remove(curr_anti_diagonal)

    dfs(0)

    return result


if __name__ == '__main__':
    n = 4
    result = solveNQueens(n)
    print(result)
