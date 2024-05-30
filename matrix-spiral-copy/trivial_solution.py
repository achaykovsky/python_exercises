# Time Complexity O(m*n) Space: O(m*n)
def spiral_copy(inputMatrix):
    """
    left                  right
    [[1,    2,   3,  4,    5],
    [6,    7,   8,  9,   10],  top
    [11,  12,  13,  14,  15],
    [16,  17,  18,  19,  20] ]  bottom

    """

    left, right = 0, len(inputMatrix[0]) - 1
    top, bottom = 0, len(inputMatrix) - 1

    result = []
    while left <= right and top <= bottom:  # the spiral ends where left>right and top>bottom

        for col in range(left, right + 1, 1):  # going and copying through left to right directions
            result.append(inputMatrix[top][col])
        top += 1  # moving downwards

        for row in range(top, bottom + 1, 1):  # going and copying from top to bottom directions
            result.append(inputMatrix[row][right])
        right -= 1  # moving to the left

        for col in range(right, left - 1, -1):  # going and copying from right to left directions
            result.append(inputMatrix[bottom][col])
        bottom -= 1  # moving up

        for row in range(bottom, top - 1, -1):  # going and copying from bottom to top directions
            result.append(inputMatrix[row][left])
        left += 1  # moving right

    return result


if __name__ == '__main__':
    inputMatrix = [[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]]
    result = spiral_copy(inputMatrix)
    print(result)
