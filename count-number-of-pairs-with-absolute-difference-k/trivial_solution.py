from typing import List


def solution(nums: List[int], k: int) -> int:
    result = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (abs(nums[i] - nums[j]) == k) and (i < j):
                result += 1

    return result


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 4]
    k = 2
    result = solution(nums, k)
    print(result)
