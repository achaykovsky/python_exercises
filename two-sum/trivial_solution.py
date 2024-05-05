# This is a generic file for the trivial solution
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    result = []
    for i in range(len(nums)):
        first_element = nums[i]
        second_element = target - first_element
        for j in range(len(nums)):
            # avoid adding answer on the second time
            if len(result) > 0:
                break
            # avoid using the same element
            if (i != j) and nums[j] == second_element:
                result.append(i)
                result.append(j)
    return result


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = twoSum(nums, target)
    print(result)
