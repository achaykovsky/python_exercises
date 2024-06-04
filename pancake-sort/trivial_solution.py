from typing import List


def pancake_sort(arr: List[int]) -> List[int]:
    n = len(arr) - 1
    for i in range(n, -1, -1):
        max_index = find_max_index(arr, i)  # find the index of the max element
        arr = flip(arr, max_index)  # flip so the max element of the sub array to make it first
        arr = flip(arr, i)  # flip the part until i to make the first element (max) as the last element

    return arr


def find_max_index(arr: List[int], k) -> int:
    ans = 0
    for i in range(0, k + 1):  # k+1 in order to include the last number as well [0,k]
        if arr[i] > arr[ans]:
            ans = i
    return ans


def flip(arr: List[int], k: int) -> List[int]:
    array_to_flip = arr[:k + 1]  # k+1 in order to include the last number as well [0,k]
    flipped_part = array_to_flip[::-1]
    remainder = arr[k + 1:]  # k+1 in order to include the last number as well [k+1,ending]
    return flipped_part + remainder

    # # to make it more space efficient we can flip by the standard algorithm of swapping:
    # if k >= 1:
    #     for i in range(1, k + 1):
    #         temp = arr[i - 1]
    #         arr[i - 1] = arr[i]
    #         arr[i] = temp
    # return arr


if __name__ == '__main__':
    arr = [1, 5, 4, 3, 2]
    result = pancake_sort(arr)
    print(result)
