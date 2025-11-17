from collections import Counter
from typing import List


# Time Complexity: O(m+n)
# Space Complexity: O(m+n)
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_counter = Counter(nums1)
    nums2_counter = Counter(nums2)
    result = []

    for k, v in nums1_counter.items():
        if k in nums2_counter.keys():
            intersected_v = min(nums1_counter[k], nums2_counter[k])  # the intersection will be the minimum occurrences
            result.extend([k] * intersected_v)  # adding the key, v times

    return result


if __name__ == '__main__':
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    result = intersect(nums1, nums2)
    print(result)
