def getConcatenation(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    result = [None] * len(nums) * 2
    n = len(nums)
    for i in range(n):
        result[i] = nums[i]
        result[i + n] = nums[i]
    return result


if __name__ == '__main__':
    nums = [1, 3, 2]
    result = getConcatenation(nums)
    print(result)
