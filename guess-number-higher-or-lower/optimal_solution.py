# This is a generic file for the trivial solution
###############################
# Simulating API

PICK = 1


def guess(num: int) -> int:
    if num > PICK:
        return -1
    elif num < PICK:
        return 1
    return 0


###############################

# Time Complexity: O(logn)
# Space Complexity: O(1)
def guessNumber(n: int) -> int:
    l, r = 1, n

    while l <= r:
        m = int((l + r) / 2)
        pick = guess(m)
        if pick == 0:
            return m
        elif pick == -1:  # higher
            r = m - 1
        else:  # lower
            l = m + 1


if __name__ == '__main__':
    n = 1

    result = guessNumber(n)
    print(result)
