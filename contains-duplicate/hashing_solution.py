from typing import List


# Time Complexity: O(n)
# Space Complexity: O(n)
def solution(nums: List[int]) -> bool:
    nums_counter_dict = {}
    for num in nums:
        nums_counter_dict[num] = 0

    for num in nums:
        nums_counter_dict[num] += 1

    for counter in nums_counter_dict.values():
        if counter > 1:
            return True

    return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    result = solution(nums)
    print(result)
