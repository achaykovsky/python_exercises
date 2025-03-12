from typing import List


# Time complexity: O(n^2), O(n) (when the list is already sorted)
# Space Complexity: O(1)
def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == '__main__':
    arr = [5, 7, 9, 1, 2]
    result = bubble_sort(arr)
    print(result)
