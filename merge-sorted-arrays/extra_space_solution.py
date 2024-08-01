# This is a generic file for the trivial solution
import heapq
from typing import List


# Time Complexity: O(m+n)
# Space: O(m+n)
def merge_sorted_arrays(array1: List[int], array2: List[int]) -> List[int]:
    result = []
    array1_length, array2_length = len(array1), len(array2)
    p1, p2 = 0, 0

    # This block will work fully on same size arrays
    while p1 < array1_length and p2 < array2_length:
        if array1[p1] == array2[p2]:
            result.append(array1[p1])
            result.append(array2[p2])
        elif array1[p1] > array2[p2]:  # the equation will decide the order of the insertion of the numbers
            result.append(array2[p2])
            result.append(array1[p1])
        else:
            result.append(array1[p1])
            result.append(array2[p2])
        p2 += 1
        p1 += 1

    while p1 < array1_length:  # adding all the rest of array1, if we didn't reach the ending before
        result.append(array1[p1])
        p1 += 1

    while p2 < array2_length:  # adding all the rest of array2, if we didn't reach the ending before
        result.append(array2[p2])
        p2 += 1

    return result


if __name__ == '__main__':
    array1 = [1, 2, 7, 8, 9]
    array2 = [0, 1, 3]
    result = merge_sorted_arrays(array1, array2)
    print(result)
