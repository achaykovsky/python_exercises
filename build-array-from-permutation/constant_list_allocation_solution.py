def buildArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    result = [None]*1000
    for i in range(len(nums)):
        result[i] = nums[nums[i]]
    result = result[:len(nums)]
    return result


if __name__ == '__main__':
    nums = [0, 2, 1, 5, 3, 4]
    result = buildArray(nums)
    print(result)
