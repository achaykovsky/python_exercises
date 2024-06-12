# This is a generic file for the trivial solution
from typing import List


# Time Complexity: O(nlogn) Space: O(m+n)
def merge_sorted_arrays(array1: List[int], array2: List[int]) -> List[int]:
    result = []
    result.extend(array1)
    result.extend(array2)
    result.sort()
    return result


if __name__ == '__main__':
    array1 = [1, 2, 3]
    array2 = [1, 1, 3]
    result = merge_sorted_arrays(array1, array2)
    print(result)
