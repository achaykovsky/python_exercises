# Array Quadruplet
from typing import List


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    result = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                for l in range(len(nums)):
                    temp_sum = sum([nums[i], nums[j], nums[k], nums[l]])
                    if i < j < k < l and temp_sum == target:
                        quadruplet = [nums[i], nums[j], nums[k], nums[l]]
                        if quadruplet not in result:
                            result.append(quadruplet)

    return result


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    result = four_sum(nums, target)
    print(result)
