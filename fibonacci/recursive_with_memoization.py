# This is a generic file for the trivial solution
from collections import defaultdict


# Time complexity: O(n) Space Complexity: O(n)
def fibonacci(n: int) -> int:
    memo = defaultdict(lambda: -1)  # initializing the memo with -1
    memo[0], memo[1] = 0, 1

    def f(n, memo):
        if n == 0 or n == 1:
            return n
        if memo[n] != -1:
            return memo[n]

        result = f(n - 2, memo) + f(n - 1, memo)
        return result

    return f(n, memo)


if __name__ == '__main__':
    n = 6
    result = fibonacci(n)
    print(result)
