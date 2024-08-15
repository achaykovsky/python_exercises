from typing import List

# Time Complexity: O(n)
# Space Complexity: O(n)
def solution(nums: List[int]) -> bool:
    set_nums = set(nums)
    if len(nums) == len(set_nums):
        return False
    return True


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    result = solution(nums)
    print(result)
