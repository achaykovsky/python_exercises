from typing import List


# Time Complexity: O(n^2)
# Space Complexity: O(n)
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()  # Sort the array to make two-pointer technique feasible
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            # Skip duplicate values to avoid duplicate triplets
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == 0:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1  # Skip duplicate values
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1  # Skip duplicate values
                l += 1
                r -= 1
            elif total < 0:
                l += 1
            else:
                r -= 1

    return result


if __name__ == '__main__':
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [3, 0, -2, -1, 1, 2]
    result = threeSum(nums)
    print(result)
