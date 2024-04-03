def decompressRLElist(nums):
    result = []
    for i in range(0, len(nums), 2):
        size = nums[i]
        result.extend([nums[i + 1]] * size)
    return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    result = decompressRLElist(nums)
    print(result)
