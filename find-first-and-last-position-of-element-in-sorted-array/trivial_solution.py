from typing import List


def find_first_binary_search(nums: List[int], target: int) -> int:
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            # found a match-> continue search to the left (we search for the leftmost match)
            right = mid

    # make sure the value at the right index equals to the target
    return left if nums[left] == target else -1


def last_first_binary_search(nums: List[int], target: int) -> int:
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    while left < right:
        # bias mid to the right to avoid infinite loop when left==mid
        mid = (left + right) // 2 + 1
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            # found a match-> continue search to the right -> (we search for the rightmost match)
            left = mid

    # make sure the value at the right index equals to the target
    return right if nums[right] == target else -1


# Time Complexity: O(logn)
# Space Complexity: O(1)

def searchRange(nums: List[int], target: int) -> List[int]:
    first_occurrence = find_first_binary_search(nums, target)
    last_occurrence = last_first_binary_search(nums, target)
    return [first_occurrence, last_occurrence]


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 2
    result = searchRange(nums, target)
    print(result)
