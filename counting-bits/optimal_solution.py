from typing import List


# Explanation:
# First iteration
# 0 - 0
# 1 - 1
# second iteration - (2-3) will include the same bits but with 1 in the beginning
# 2 - 10 - 1 0
# 3 - 11 - 1 1

# Next iteration (4-7) will include the same bits but with 1 in the beginning
# 100 = 1 00
# 101 = 1 01
# 110 = 1 10
# 111 = 1 11

# and so on

def countBits(n: int) -> List[int]:
    result = [0] * (n + 1)
    off = 1  # offset

    for i in range(1, n + 1):
        if off * 2 == i:  # we reached the new binary limit of numbers that repeat themselves
            off = i
        result[i] = 1 + result[i - off]  # each number will have the same number of 1's as in previous iteration + 1

    return result


if __name__ == '__main__':
    n = 5
    result = countBits(n)
    print(result)
