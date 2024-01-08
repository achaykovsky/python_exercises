def getConcatenation(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    result = 2 * nums
    return result


if __name__ == '__main__':
    nums = [1, 3, 2]
    result = getConcatenation(nums)
    print(result)