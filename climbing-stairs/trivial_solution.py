
def climbStairs(n: int) -> int:
    # Base Case: not moving or taking one step
    if n == 0 or n == 1:
        return 1

    # Step: Move either one step or 2 steps
    return climbStairs(n - 1) + climbStairs(n - 2)


if __name__ == '__main__':
    n = 2
    result = climbStairs(n)
    print(result)
