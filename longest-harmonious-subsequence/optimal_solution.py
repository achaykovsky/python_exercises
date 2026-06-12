from collections import Counter
from typing import List


# Time Complexity: O(n)
# Space Complexity: O(n)

def findLHS(nums: List[int]) -> int:
    freq = Counter(nums)
    max_len = 0

    for num in freq:
        # existence of the next num as the key
        if num + 1 in freq:

            # find the max sum
            max_len = max(max_len, freq[num] + freq[num + 1])

    return max_len


if __name__ == '__main__':
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    result = findLHS(nums)
    print(result)
