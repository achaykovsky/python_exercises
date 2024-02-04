from typing import List


def runningSum(nums: List[int]) -> List[int]:
    result = [0] * len(nums)
    sum_of_nums = nums[0]
    result[0] = nums[0]
    for i in range(1, len(nums)):
        sum_of_nums += nums[i]
        result[i] = sum_of_nums

    return result


if __name__ == '__main__':
    nums = [3, 1, 2, 10, 1]
    result = runningSum(nums)
    print(result)
