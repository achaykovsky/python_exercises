def calculate_second_max(arr):
    first_max = max(arr)
    arr.remove(first_max)
    second_max = max(arr)
    return second_max


if __name__ == '__main__':
    array = [2, 3, 5, 4]
    result = calculate_second_max(array)
    print(result)
