from typing import List


# Checks whether cutting all trees at height H yields at least k units of wood
def cuts_k_wood(heights: List[int], H: int, k: int) -> bool:
    collected_wood = 0
    for height in heights:
        if height > H:
            # we would like to chop the top until H
            collected_wood += (height - H)
        # when height<=H, we can't collect any wood!

    # True if we can cut at least k meters from the wood
    return collected_wood >= k


# We perform binary search on the possible cutting heights (0 to max height)
# to find the maximum height at which we can still collect at least k units of wood.


# Time Complexity: O(n*logm)
# Space Complexity: O(1)
def cutting_wood(heights: List[int], k: int) -> int:
    left, right = 0, max(heights)
    while left < right:
        mid = (left + right) // 2 + 1  # bias to the right when performing an upper-bound binary search
        if cuts_k_wood(heights, mid, k):
            # Able to cut at least k meters -> try a higher cut on the right side
            left = mid
        else:
            # Unable to cut at least k meters -> try a smaller cut on the left side
            right = mid - 1
    # the upper bound will be the rightmost height that cuts k wood
    return right


if __name__ == '__main__':
    heights = [2, 6, 3, 8]
    k = 7
    result = cutting_wood(heights, k)
    print(result)
