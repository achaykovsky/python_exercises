from typing import List


def createTargetArray(nums: List[int], index: List[int]):
    result = []
    for i in range(len(nums)):
        result.insert(index[i], nums[i])
    return result


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    result = createTargetArray(nums, index)
    print(result)
