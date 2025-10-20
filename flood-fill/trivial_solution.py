from typing import List


# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

# DFS approach (recursive)
def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    start_color = image[sr][sc]
    if start_color == color:
        return image  # No need to fill if the color is the same

    def dfs(r, c):
        if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == start_color:
            image[r][c] = color
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

    dfs(sr, sc)
    return image


if __name__ == '__main__':
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    result = floodFill(image, sr, sc, color)
    print(result)
