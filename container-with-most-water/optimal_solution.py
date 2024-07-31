from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)
def maxArea(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    max_area = 0

    while l < r:
        curr_width = r - l
        curr_height = min(height[l], height[r])
        area = curr_width * curr_height
        max_area = max(max_area, area)

        if height[l] < height[r]:  # Move the pointer pointing to the shorter height to try
            # to find a taller container that might produce a larger area.
            l += 1
        else:
            r -= 1

    return max_area


if __name__ == '__main__':
    height = [1, 1]
    result = maxArea(height)
    print(result)
