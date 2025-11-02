from typing import List


# Time complexity: O(n)
# Sapce: O(1)
def search(nums: List[int], target: int) -> int:
    for index, num in enumerate(nums):
        if num == target:
            return index
    return result


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    result = search(nums, target)
    print(result)
