from typing import List


# Time Complexity: O(m+n)
# Space Complexity: O(m)
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_set = set(nums1)
    result = []

    for num in nums2:
        if num in nums1_set:
            nums1_set.remove(num)
            result.append(num)

    return result


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    result = intersection(nums1, nums2)
    print(result)
