from typing import List


# Time Complexity: O(n)
# Space Complexity:O(1)

def removeElement(nums: List[int], val: int) -> int:
    # replacing all equal numbers with placeholder
    for i, num in enumerate(nums):
        if num == val:
            nums[i] = '.'

    r = len(nums) - 1
    l = 0
    counter = 0

    # going through to list and swap all the elements to the front
    while l < r:
        if nums[l] == '.' and nums[r] != '.':
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
            l += 1
        elif nums[l] == '.' and nums[r] == '.':
            r -= 1
        else:
            l += 1

    return r + 1


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    result = removeElement(nums, val)
    print(result)
