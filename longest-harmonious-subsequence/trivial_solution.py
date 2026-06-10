from typing import List


# Time Complexity: O(n^2)
# Space Complexity: O(1)

def findLHS(nums: List[int]) -> int:
    max_len = 0

    for i in range(len(nums)):
        count = 0

        for j in range(len(nums)):
            if abs(nums[i] - nums[j]) == 1:  # diff of 1
                count += 1
            elif nums[i] == nums[j]:  # count equal as well
                count += 1

        # Only valid if at least one different value exists
        if count > 1:
            max_len = max(max_len, count)
    return max_len


if __name__ == '__main__':
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    result = findLHS(nums)
    print(result)
