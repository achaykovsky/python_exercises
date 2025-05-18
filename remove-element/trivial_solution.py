from typing import List


# Time Complexity: O(n^2)
# Space Complexity:O(1)
def removeElement(nums: List[int], val: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    result = removeElement(nums, val)
    print(result)
