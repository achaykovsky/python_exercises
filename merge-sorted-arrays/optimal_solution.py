from typing import List


# Time Complexity: O(num1_length + num2_length)
# Space: O(1)
def merge_sorted_arrays(nums1: List[int], num1_length: int, nums2: List[int], num2_length: int) -> None:
    end = num1_length + num2_length - 1  # last element index

    while num2_length > 0 and num1_length > 0:
        if nums1[num1_length - 1] > nums2[num2_length - 1]:
            nums1[end] = nums1[num1_length - 1]
            num1_length -= 1
        else:
            nums1[end] = nums2[num2_length - 1]
            num2_length -= 1
        end -= 1

    while num2_length > 0:
        nums1[end] = nums2[num2_length - 1]
        end -= 1
        num2_length -= 1

    return nums1


if __name__ == '__main__':
    array1 = [1, 2, 3, 0, 0, 0]  # we have enough space to add array2
    array2 = [2, 2, 2]
    result = merge_sorted_arrays(array1, 3, array2, 3)
    print(result)
