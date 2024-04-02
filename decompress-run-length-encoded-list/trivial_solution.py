def decompressRLElist(nums):
    result = []
    for i in range(0, len(nums) - 1, 2):
        size = nums[i]
        for index in range(size):
            result.append(nums[i + 1])
    return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    result = decompressRLElist(nums)
    print(result)
