# This is a generic file for the trivial solution
from typing import List


def binary_search(numbers: List[int], second_num: int) -> int:
    l, r = 0, len(numbers) - 1
    result = -1

    while l <= r:
        m = (l + r) // 2
        if numbers[m] == second_num:
            result = m
            return result
        elif numbers[m] < second_num:
            l = m + 1
        else:
            r = m - 1

    return result


# Time Complexity: O(nlogn)
# Space Complexity: O(1)
def twoSum(numbers: List[int], target: int) -> List[int]:
    result = [-1]
    for i, num in enumerate(numbers):
        second_num = target - num
        second_num_index = binary_search(numbers[i + 1:], second_num) + (i + 1)
        if second_num_index == -1:
            continue
        if i < second_num_index and second_num_index != -1:
            result = [i + 1, second_num_index + 1]
            return result

    return result


if __name__ == '__main__':
    # numbers = [5, 25, 75]
    # target = 100

    # numbers = [2, 7, 11, 15]
    # target = 9

    # numbers = [1, 2, 3, 4, 4, 9, 56, 90]
    # target = 8

    numbers = [2, 3, 4]
    target = 6
    result = twoSum(numbers, target)
    print(result)
