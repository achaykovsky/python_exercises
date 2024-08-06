# Array Quadruplet
from typing import List


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    result = []
    nums.sort()

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            l, r = j + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[j] + nums[r] + nums[l]
                if total == target:
                    result.append([nums[i], nums[j], nums[r], nums[l]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total > target:
                    r -= 1
                else:
                    l += 1

    return result


if __name__ == '__main__':
    nums = [-2, -1, -1, 1, 1, 2, 2]
    target = 0
    result = four_sum(nums, target)
    print(result)
