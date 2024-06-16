from typing import List


# Time Complexity: O(m*n)
# Space Complexity: O(1)
def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
    rows_length = len(matrix) - 1
    cols_length = len(matrix[0]) - 1

    corners = [(rows_length, 0), (0, cols_length)]  # two corners that are not the beginning of a diagonal

    for r in range(rows_length):
        for c in range(cols_length):
            if (r, c) not in corners:  # skipping the two corners that are not the beginning of a diagonal
                if matrix[r][c] != matrix[r + 1][c + 1]:  # validating the diagonal
                    return False

    return True


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    # matrix = [[1, 2], [2, 2]]
    result = isToeplitzMatrix(matrix)
    print(result)
