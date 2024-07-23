from typing import List


def findPairs(nums: List[int], k: int) -> int:
    result = []
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if i != j and num1 - num2 == k:
                if [num1, num2] not in result:
                    result.append([num1, num2])

    return result


if __name__ == '__main__':
    nums = [1, 3, 1, 5, 4]
    k = 0
    result = findPairs(nums, k)
    print(result)
