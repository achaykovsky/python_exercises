from typing import List


# Time Complexity: O(n)
# Space Complexity: O(n)
def sumZero(n: int) -> List[int]:
    result = []
    num = 1

    # adding pairs of nums and their negatives
    for i in range(1, n, 2):
        result.append(num)
        result.append(-num)
        num += 1

    # odd n -> add zero
    if n % 2 != 0:
        result.append(0)

    return result


if __name__ == '__main__':
    n = 5
    result = sumZero(n)
    print(result)
