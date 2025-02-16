# The "Climbing Stairs" problem is a Fibonacci problem
# because the number of ways to reach step n.
# n depends directly on the ways to reach the two preceding steps, n-1 and n-2
# f(n) = f(n-1) + f(n-2)
def climbStairs(n: int) -> int:
    if n <= 1:
        return 1

    # Base cases: f(0) = 1, f(1) = 1
    prev, curr = 1, 1
    for _ in range(2, n + 1):
        # Update to the next Fibonacci number
        prev, curr = curr, prev + curr

    return curr


if __name__ == '__main__':
    n = 2
    result = climbStairs(n)
    print(result)
