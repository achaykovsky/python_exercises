from typing import List


def diagonalSum(mat: List[List[int]]) -> int:
    size = len(mat)
    primary_diagonal, secondary_diagonal = 0, 0
    for i in range(len(mat)):
        primary_diagonal += mat[i][i]
        secondary_diagonal += mat[i][size - i - 1]

    result = primary_diagonal + secondary_diagonal
    if size % 2 != 0:
        result -= mat[size // 2][size // 2]

    return result


if __name__ == '__main__':
    mat = [[7, 3, 1, 9], [3, 4, 6, 9], [6, 9, 6, 6], [9, 5, 8, 5]]
    result = diagonalSum(mat)
    print(result)
