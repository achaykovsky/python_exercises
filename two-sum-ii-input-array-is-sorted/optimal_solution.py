# This is a generic file for the trivial solution
from typing import List


# Time Complexity: O(n) Space Complexity: O(1)
# two pointer solution
def twoSum(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1

    while l < r:
        sum = numbers[l] + numbers[r]
        if sum == target:
            return [l + 1, r + 1]
        elif sum > target:
            r -= 1
        else:
            l += 1

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
