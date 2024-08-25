from typing import List

# Time Complexity: O(n)
# Space Complexity: O(k)
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    near_numbers = set()
    l, r = 0, k

    for r in range(len(nums)):
        if r - l > k:  # the window is bigger than k
            near_numbers.remove(nums[l])
            l += 1
        if nums[r] in near_numbers:  # found a duplicate
            return True
        near_numbers.add(nums[r])  # moving forward the window
    return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    result = containsNearbyDuplicate(nums, k)
    print(result)
