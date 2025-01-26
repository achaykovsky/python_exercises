# This is a generic file for the trivial solution
from collections import Counter
from typing import List


# Time Complexity: O(n)
# Space Complexity: O(n)
def uniqueOccurrences(arr: List[int]) -> bool:
    array_counter = Counter(arr)

    occurrences = list(array_counter.values())

    set_occurrences = set(array_counter.values())

    # if after converting to set we have less numbers, it means we had a few occurrences -> not unique
    if len(occurrences) == len(set_occurrences):
        return True

    return False


if __name__ == '__main__':
    arr = [2, 2]
    result = uniqueOccurrences(arr)
    print(result)
