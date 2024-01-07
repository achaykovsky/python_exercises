def getConcatenation(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.extend(nums)
    return nums


if __name__ == '__main__':
    nums = [1, 3, 2]
    result = getConcatenation(nums)
    print(result)
