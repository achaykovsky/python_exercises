# This is a generic file for the trivial solution

def solution(nums):
    non_zero_index = 0  # the next index that should not be zero
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1

    return numbers


if __name__ == '__main__':
    numbers = [0, 1, 0, 3, 12]
    result = solution(numbers)
    print(result)
