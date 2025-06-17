import collections
from typing import List


# Time Complexity: O(n)
# Space Complexity: O(n)
def missingNumber(nums: List[int]) -> int:
    counter = collections.Counter(nums)

    for i in range(len(nums)):
        if counter[i] == 0:
            return i

    return len(nums)


if __name__ == '__main__':
    nums = [3, 0, 1]
    result = missingNumber(nums)
    print(result)
