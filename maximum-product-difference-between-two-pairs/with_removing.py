from typing import List


# all the max/min operations are O(n)
# the remove operation also is O(n)
def maxProductDifference(nums: List[int]) -> int:
    first_max = max(nums)
    first_min = min(nums)

    nums.remove(first_max)
    nums.remove(first_min)

    second_max = max(nums)
    second_min = min(nums)

    return first_max * second_max - first_min * second_min


if __name__ == '__main__':
    nums = [5, 6, 2, 7, 4]
    result = maxProductDifference(nums)
    print(result)
