from typing import List

# Time Complexity: O(n^2)
# Space Complexity: O(1)
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] == nums[j] and abs(i - j) <= k:
                return True
    return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    k = 3
    result = containsNearbyDuplicate(nums, k)
    print(result)
