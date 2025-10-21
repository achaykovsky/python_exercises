from typing import List


# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

# BFS approach (iterative)
def flood_fill(image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
    rows, cols = len(image), len(image[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    color = image[sr][sc]

    if color == new_color:
        return image  # No need to change the color if it's already the new color

    queue = [(sr, sc)]
    image[sr][sc] = new_color

    while queue:
        r, c = queue.pop(0)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == color:
                queue.append((nr, nc))
                image[nr][nc] = new_color

    return image


if __name__ == '__main__':
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    result = flood_fill(image, sr, sc, color)
    print(result)
