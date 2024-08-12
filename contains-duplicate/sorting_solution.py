from typing import List


# Time Complexity: O(nlogn)
# Space Complexity: O(1)
def solution(nums: List[int]) -> bool:
    nums.sort()

    for i in range(len(nums)):
        if nums[i] == nums[i - 1]:
            return True

    return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    result = solution(nums)
    print(result)
