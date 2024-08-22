from typing import List

# Time Complexity: O(n^2)
# Space Complexity: O(1)
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    for l in range(len(nums) - 1):
        for r in range(l + 1, min(l + k + 1, len(nums))):
            if nums[l] == nums[r] and l < r:
                return True

    return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    result = containsNearbyDuplicate(nums, k)
    print(result)
