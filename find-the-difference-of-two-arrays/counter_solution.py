from collections import Counter
from typing import List


# Time Complexity: O(n+m)
# Space Complexity: O(n+m)

def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    counter1 = Counter(nums1)
    counter2 = Counter(nums2)

    res1, res2 = [], []

    for num1 in nums1:
        if num1 not in counter2 and num1 not in res1:
            res1.append(num1)

    for num2 in nums2:
        if num2 not in counter1 and num2 not in res2:
            res2.append(num2)

    return [res1, res2]


if __name__ == '__main__':
    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]
    result = findDifference(nums1, nums2)
    print(result)
