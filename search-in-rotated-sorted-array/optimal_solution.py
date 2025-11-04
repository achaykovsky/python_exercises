from typing import List


# Time complexity: O(nlogn)
# Space: O(1)
def search(nums: List[int], target: int) -> int:
    result = -1

    if len(nums) == 0:
        return result

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # if the left part is sorted -> leftmost will be smaller than the mid!
        elif nums[left] <= nums[mid]:

            # perform a binary search
            if nums[left] <= target and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # the right number is bigger than the mid, so the right part is sorted
        else:
            # perform a binary search
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    if nums[left] == target:
        result = left
    return result


if __name__ == '__main__':
    nums = [5, 1, 3]
    target = 3
    result = search(nums, target)
    print(result)
