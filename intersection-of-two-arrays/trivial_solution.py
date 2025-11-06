from typing import List


# Time Complexity: O(m+n)
# Space Complexity: O(m+n)
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_set = set(nums1)
    nums2_set = set(nums2)

    nums_intersection = nums1_set.intersection(nums2_set)

    return list(nums_intersection)


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    result = intersection(nums1, nums2)
    print(result)
