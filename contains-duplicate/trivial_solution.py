from typing import List


# Time Complexity: O(n^2)
# Space Complexity: O(1)
def solution(nums: List[int]) -> bool:
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if i > j:
                if num1 == num2:
                    return True

    return False


if __name__ == '__main__':
    nums = [1, 2, 3]
    result = solution(nums)
    print(result)
