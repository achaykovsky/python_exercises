from typing import Set


# N-Queens Problem: Count the number of distinct solutions to the N-Queens problem.
# diagonals are from left to right (row-col)
# anti-diagonals are from right to left (row+col)


# Time Complexity: O(n!), where n is the number of queens
# Space Complexity: O(n), for the recursion stack and the sets used to track columns and diagonals.
def totalNQueens(n: int) -> int:
    def dfs(row: int, cols: Set[int], diagonals: Set[int], anti_diagonals: Set[int]) -> int:
        if row == n:
            return 1

        count = 0

        for col in range(n):
            cur_diagonal = row - col
            cur_anti_diagonal = row + col

            # Check if the column or diagonals are already occupied
            if (col in cols or
                    cur_diagonal in diagonals or
                    cur_anti_diagonal in anti_diagonals):
                continue

            # Try to place a queen
            cols.add(col)
            diagonals.add(cur_diagonal)
            anti_diagonals.add(cur_anti_diagonal)

            count += dfs(row + 1, cols, diagonals, anti_diagonals)

            # Remove the queen from the board
            cols.remove(col)
            diagonals.remove(cur_diagonal)
            anti_diagonals.remove(cur_anti_diagonal)

        return count

    return dfs(0, set(), set(), set())


if __name__ == '__main__':
    n = 4
    result = totalNQueens(n)
    print(result)
