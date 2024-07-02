# This is a generic file for the trivial solution
from typing import List


# Time Complexity: O(n^2) Space Complexity: O(1)
def two_sum(numbers: List[int], target: int) -> List[int]:
    for i in range(0, len(numbers)):
        for j in range(1, len(numbers)):
            sum_result = numbers[i] + numbers[j]
            if i < j and sum_result == target:
                return [i + 1, j + 1]


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    result = two_sum(numbers, target)
    print(result)
