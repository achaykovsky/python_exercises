from typing import List


# Time Complexity: O(n+m)
# Space Complexity: O(n+m)

def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    num1_set = set(nums1)
    num2_set = set(nums2)

    difference_1 = num1_set.difference(num2_set)  # O(n)
    difference_2 = num2_set.difference(num1_set)  # O(m)

    return [list(difference_1), list(difference_2)]


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    result = findDifference(nums1, nums2)
    print(result)
