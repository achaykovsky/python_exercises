# This is a generic file for the trivial solution
from collections import defaultdict


# Time complexity: O(n) Space Complexity: O()
def fibonacci(n: int) -> int:
    sum = 0
    i1, i2 = 0, 1

    if n <= 1:  # if the n=1 or n=0 - nothing to calculate
        return n

    # calculating starting 2
    while n >= 2:  ###equialant to:  for _ in range(2,n+1)
        sum = i1 + i2
        i1 = i2
        i2 = sum
        n -= 1

    return sum


if __name__ == '__main__':
    n = 5
    result = fibonacci(n)
    print(result)
