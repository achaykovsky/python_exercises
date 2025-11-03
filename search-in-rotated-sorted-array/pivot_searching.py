from typing import List


# Time Complexity: O(n)
# Space Complexity: O(n)
def search(nums: List[int], target: int) -> int:
    pivot = 0
    result = -1
    for i, num in enumerate(nums):  # In WC: O(n)
        if nums[i] > nums[i + 1] and i < len(
                nums):  # there is only one place in the array that satisfies this condition
            pivot = i
            break

    if target > nums[pivot]:  # the array is rotated so:
        result = binary_search(nums[:pivot], target)  # 1. on the left side will be the bigger numbers
    else:
        result = binary_search(nums[pivot:], target) + pivot  # 2. on the right side will be the smaller numbers
        # we add the pivot since the array we send to the BS will start from 0 and it should be moved by the rotation step

    return result


def binary_search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            l = m + 1
        else:
            r = m - 1
    return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    result = search(nums, target)
    print(result)
