def calculate_second_max(arr):
    if arr[0] > arr[1]:
        first_max = arr[0]
        second_max = arr[1]
    else:
        first_max = arr[1]
        second_max = arr[0]
    for i in range(len(arr) - 1):
        if first_max >= arr[i + 1]:
            if second_max < arr[i + 1]:
                second_max = arr[i + 1]
        elif first_max < arr[i + 1]:
            second_max = first_max
            first_max = arr[i + 1]

    return second_max


if __name__ == '__main__':
    array = [2, 3, 5, 4]
    result = calculate_second_max(array)
    print(result)
