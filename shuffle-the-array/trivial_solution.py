# This is a generic file for the trivial solution

def shuffle(nums, n):
    first_n_numbers = nums[:n]
    last_n_numbers = nums[n:]
    result = []
    for i, j in zip(first_n_numbers, last_n_numbers):
        result.append(i)
        result.append(j)

    return result


if __name__ == '__main__':
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    result = shuffle(nums, n)
    print(result)
