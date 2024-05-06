from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    result = []

    # building hashmap that for each element has it index and the substraction result
    substraction_results = {num: (i, target - num) for i, num in zip(range(len(nums)), nums)}

    for i in range(len(nums)):
        res = target - nums[i]
        if res in substraction_results:
            index_second_element = substraction_results[res][0]
            # avoiding using the same element
            if index_second_element != i:
                result.append(i)
                result.append(index_second_element)
                return result
    return result


if __name__ == '__main__':
    nums = [0, 4, 3, 0]
    target = 0
    result = twoSum(nums, target)
    print(result)
