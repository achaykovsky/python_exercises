from typing import List


def minOperations(nums: List[int]) -> int:
    result = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            continue
        elif nums[i] == nums[i - 1]:
            diff = 1
        else:
            diff = (nums[i - 1] - nums[i]) + 1
        nums[i] += diff
        result += diff
    return result


if __name__ == '__main__':
    nums = [1, 5, 2, 4, 1]
    result = minOperations(nums)
    print(result)
