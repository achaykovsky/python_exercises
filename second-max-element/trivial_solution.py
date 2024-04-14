# This is a generic file for the trivial solution

def calculate_second_max(arr):
    sorted_array = sorted(arr)
    return sorted_array[-2]


if __name__ == '__main__':
    array = [2, 3, 5, 4]
    result = calculate_second_max(array)
    print(result)
