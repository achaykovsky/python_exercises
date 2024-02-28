from typing import List


def countGoodTriplets(arr: List[int], a: int, b: int, c: int) -> int:
    result = []
    for i in range(0, len(arr)):
        for j in range(1, len(arr)):
            for k in range(2, len(arr)):
                if (i < j < k
                        and abs(arr[i] - arr[j]) <= a
                        and abs(arr[j] - arr[k]) <= b
                        and abs(arr[i] - arr[k]) <= c):
                    result.append([arr[i], arr[j], arr[k]])

    return len(result)


if __name__ == '__main__':
    arr = [3, 0, 1, 1, 9, 7]
    a = 7
    b = 2
    c = 3
    result = countGoodTriplets(arr, a, b, c)
    print(result)
