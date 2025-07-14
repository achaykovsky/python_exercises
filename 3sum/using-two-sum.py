from typing import List


# The goal is to find triplets that sum to 0 (nums[i]+nums[j]+nums[k]=0)


def find_all_pairs_sum_sorted(nums: List[int], start: int, target: int) -> List[List[int]]:
    left, right = start, len(nums) - 1
    pairs = []

    while left < right:
        pair_sum = nums[left] + nums[right]
        if pair_sum == target:
            pairs.append([nums[left], nums[right]])
            left += 1

            # Make sure no duplicated on the second number for [nums[j],nums[k]]
            # if it's the same as the previous number
            while left < right and nums[left] == nums[left - 1]:
                left += 1

        elif pair_sum > target:
            right -= 1
        elif pair_sum < target:
            left += 1
    return pairs


# Time Complexity: O(n^2)
# Space Complexity: O(n) - for the sorting algorithm

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()  # Sort the array to make two-pointer technique feasible
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            # Skip duplicate values to avoid duplicate triplets
            continue

        # start from the next index
        # nums[i] + nums[j] + nums[k] = 0 => nums[j] + nums[k] = -nums[i]
        pairs = find_all_pairs_sum_sorted(nums, i + 1, -nums[i])

        # add nums[i] to all the pairs we've found
        for pair in pairs:
            result.append([[nums[i]] + pair])

    return result


if __name__ == '__main__':
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [3, 0, -2, -1, 1, 2]
    result = threeSum(nums)
    print(result)
