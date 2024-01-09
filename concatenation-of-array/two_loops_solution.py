def getConcatenation(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    result = []
    n = len(nums)
    for times in range(2):
        for index in range(n):
            result.append(nums[index])
    return result


if __name__ == '__main__':
    nums = [1, 3, 2]
    result = getConcatenation(nums)
    print(result)
