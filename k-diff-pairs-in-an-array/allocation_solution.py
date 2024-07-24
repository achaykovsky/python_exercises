
from collections import defaultdict, Counter
from typing import List


def findPairs(nums: List[int], k: int) -> int:
    solutions_hashmap = defaultdict()
    pairs_list = []
    result = 0

    count = Counter(nums)

    if k == 0:  # the second solution will create a pair for each pair without a unique solution for the 0
        for num in count:
            if count[num] > 1:
                result += 1
    else:  # different approach for k>0
        for element in nums:
            solutions_hashmap[element - k] = element

        for element in nums:
            if element in solutions_hashmap.keys():
                value = solutions_hashmap.get(element)
                if [value, element] not in pairs_list:
                    pairs_list.append([value, element])

        result = len(pairs_list)
    return result


if __name__ == '__main__':
    nums = [1, 3, 1, 5, 4]
    k = 0
    result = findPairs(nums, k)
    print(result)
