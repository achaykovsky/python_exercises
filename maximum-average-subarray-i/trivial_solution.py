from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    average = float("-infinity")
    if len(nums) == 1:
        return nums[0]

    for i in range(len(nums) - 1):
        curr_sum = 0
        if i + k - 1 < len(nums):
            curr_sum = sum(nums[i: i + k])
            average = max(average, curr_sum / k)
    return average


if __name__ == '__main__':
    nums = [0, 1, 1, 3, 3]
    k = 4
    result = findMaxAverage(nums, k)
    print(result)
