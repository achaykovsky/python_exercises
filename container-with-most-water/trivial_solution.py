from typing import List


# Time Complexity: O(n^2)
# Space Complexity: O(1)
def maxArea(height: List[int]) -> int:
    max_area = 0
    for i1, h1 in enumerate(height):
        for i2, h2 in enumerate(height):
            if i1 < i2:
                width = i2 - i1
                area = width * min(h1, h2)  # the height here will be the minimum between the two endpoints
                max_area = max(max_area, area)
    return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = maxArea(height)
    print(result)
