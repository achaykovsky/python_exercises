from typing import List


def runningSum(nums: List[int]) -> List[int]:
    result = []
    for i in range(1, len(nums)+1):
        summary = sum(nums[:i])
        result.append(summary)
    return result


if __name__ == '__main__':
    nums = [3, 1, 2, 10, 1]
    result = runningSum(nums)
    print(result)
