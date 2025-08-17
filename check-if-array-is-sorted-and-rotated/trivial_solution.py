from typing import List


# The idea is:
# 1. Array Sorted - 0 cliffs
# 2. Rotated Array - 1 cliff at most
# 3. 2+ or more cliffs, it can't be a single rotation


# Time Complexity: O(n)
# Space Complexity: O(1)
def check(nums: List[int]) -> bool:
    cliff = 0
    n = len(nums)

    for i in range(n):
        # will compare the first with the last in the end
        if nums[i] > nums[(i + 1) % n]:
            cliff += 1
            if cliff > 1:
                return False
    return True


if __name__ == '__main__':
    nums = [2, 1, 3, 4]
    result = check(nums)
    print(result)
