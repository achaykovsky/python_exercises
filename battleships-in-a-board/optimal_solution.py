from typing import List


# Time Complexity: O(m*n)
# Space Complexity: O(1)
def countBattleships(board: List[List[str]]) -> int:
    counter = 0
    rows = len(board)
    cols = len(board[0])

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "X":
                # Check if it is the start of a battleship
                if (r == 0 or board[r - 1][c] == ".") and (
                        c == 0 or board[r][c - 1] == "."
                ):
                    counter += 1

    return counter


if __name__ == '__main__':
    board = [["X", ".", ".", "X"],
             [".", ".", ".", "X"],
             [".", ".", ".", "X"]]
    result = countBattleships(board)
    print(result)
