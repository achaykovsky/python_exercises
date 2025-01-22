# This is a generic file for the trivial solution
from collections import Counter
from typing import List


# Time Complexity: O(nlogn)
# Space Complexity: O(n)
def uniqueOccurrences(arr: List[int]) -> bool:
    array_counter = Counter(arr)

    sorted_values = sorted(array_counter.values())  # we must sort in case we will have values of 1,2,1 for example

    for i in range(len(sorted_values)):
        # if we found equal occurrence ->it is not unique
        # for the case of only one number we have unique occurrence
        if sorted_values[i] == sorted_values[i - 1] and len(sorted_values) > 1:
            return False

    return True


if __name__ == '__main__':
    arr = [2, 2]
    result = uniqueOccurrences(arr)
    print(result)
