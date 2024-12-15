from typing import List


# leetcode 2215

# Time Complexity: O(n*m)
# Space: O(n+m)
def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    res_nums1 = []
    res_nums2 = []
    found = False

    for num1 in nums1:
        for num2 in nums2:
            if num1 == num2:
                found = True
                continue
        if not found:
            res_nums1.append(num1)
        found = False

    for num2 in nums2:
        for num1 in nums1:
            if num1 == num2:
                found = True
                continue
        if not found:
            res_nums2.append(num2)
        found = False

    result = [res_nums1, res_nums2]

    return result


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    result = findDifference(nums1, nums2)
    print(result)
