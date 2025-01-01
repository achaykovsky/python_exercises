from typing import List


# Time Complexity: O(n+m)
# Space Complexity: O(n+m)

def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    nums1_set, nums2_set = set(nums1), set(nums2)

    res1, res2 = set(), set()

    for num1 in nums1:
        if num1 not in nums2_set:
            res1.add(num1)

    for num2 in nums2:
        if num2 not in nums1_set:
            res2.add(num2)

    return [list(res1), list(res2)]


if __name__ == '__main__':
    nums1 = [1, 2, 3, 5]
    nums2 = [7, 2, 4, 6]
    result = findDifference(nums1, nums2)
    print(result)
