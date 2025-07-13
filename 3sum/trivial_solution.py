from typing import List


# Time Complexity: O(n^3)
# Space Complexity: O(n^2)
def threeSum(nums: List[int]) -> List[List[int]]:
    result = set()
    num_length = len(nums)
    for i in range(num_length):
        for j in range(num_length):
            for k in range(num_length):
                if i < j < k and nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    if triplet not in result:
                        result.add(triplet)

    return [list(triplet) for triplet in result]


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    result = threeSum(nums)
    print(result)
