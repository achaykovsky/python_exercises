# Time complexity: O(nlogn)
# Space Complexity: O(n)
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


# Time complexity: O(n)
# Space Complexity: O(n)
def merge(left: List[int], right: List[int]) -> List[int]:
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # Ensures stability
            # stable means it preserves the relative order of equal elements in the original array
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Append remaining elements
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


if __name__ == '__main__':
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sort(arr)
    print(sorted_arr)  # Output: [3, 9, 10, 27, 38, 43, 82]
