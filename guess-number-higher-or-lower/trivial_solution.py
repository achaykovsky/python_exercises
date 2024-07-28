# This is a generic file for the trivial solution
###############################
# Simulating API

PICK = 6


def guess(num: int) -> int:
    if num > PICK:
        return -1
    elif num < PICK:
        return 1
    return 0


###############################

# Time Complexity: O(n)
# Space Complexity: O(1)
def guessNumber(n: int) -> int:
    i = 0

    while i <= n:
        curr_guess = guess(i)
        if curr_guess == 0:
            return i
        i += 1


if __name__ == '__main__':
    n = 10

    result = guessNumber(n)
    print(result)
