from typing import List


# Time Complexity: O(m*n)
# Space Complexity: O(1)
def findDiagonalOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    result = []

    row, col = 0, 0
    direction = 1  # 1 = up-right, -1 = down-left

    for _ in range(rows * cols):
        result.append(matrix[row][col])

        if direction == 1:  # Moving up-right

            if col == cols - 1:
                row += 1
                direction *= -1  # hit the wall -> change direction
            elif row == 0:
                col += 1
                direction *= -1  # hit the wall -> change direction

            # didn't hit the wall
            else:
                row -= 1
                col += 1

        else:  # Moving down-left

            if row == rows - 1:
                col += 1
                direction *= -1  # hit the wall -> change direction
            elif col == 0:
                row += 1
                direction *= -1  # hit the wall -> change direction

            # didn't hit the wall
            else:
                row += 1
                col -= 1

    return result


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = findDiagonalOrder(matrix)
    print(result)
