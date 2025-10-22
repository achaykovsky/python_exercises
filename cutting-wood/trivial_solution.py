from typing import List


# Time Complexity: O(n*max_height)
# Space Complexity: O(1)
def cutting_wood(heights: List[int], k: int) -> int:
    max_height = max(heights)
    # Looking for the highest possible cut_candidate -> Start from the top
    for cut_candidate in range(max_height, -1, -1):
        total_sum = 0
        for height in heights:
            if height > cut_candidate:
                # adding the difference we can cut from this tree
                total_sum += height - cut_candidate
            # if the height is smaller or equal to the cut_candidate it means we can't cut anything!!

        # if the total sum we cut until now is greater or equal to k -> we found our H of the woodcutter
        if total_sum >= k:
            return cut_candidate

    return -1


if __name__ == '__main__':
    heights = [2, 6, 3, 8]
    k = 7
    result = cutting_wood(heights, k)
    print(result)
