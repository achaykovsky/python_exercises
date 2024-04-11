def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    length = len(nums)
    bucket = [0] * 101
    result = 0
    for i in range(length):
        bucket[nums[i]] += 1

    for i in range(101):
        #n*(n-1) to calculate all the combinations
        #dividing by 2 to find all the pairs
        bucket[i] = (bucket[i] * (bucket[i] - 1)) // 2

    for i in range(101):
        result += bucket[i]
    return result


if __name__ == '__main__':
    # nums = [1, 2, 3]
    # nums = [1, 2, 3, 1, 1, 3]
    # nums = [1, 1, 1, 1]
    nums = [4, 4, 2, 2]
    result = numIdenticalPairs(nums)
    print(result)
