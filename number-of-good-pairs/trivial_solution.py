def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    result = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i < j:
                result += 1
    return result


if __name__ == '__main__':
    nums = [1, 2, 3, 1, 1, 3]
    result = numIdenticalPairs(nums)
    print(result)
