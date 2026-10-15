# Top Down Approach

# Time Complexity: O(2^n)
# Space Complexity: O(n)
def climbStairs(n: int) -> int:
    # Base Case: taking 1 or 2 steps results in 1 or 2 ways respectively
    if n <= 2:
        return n

    # Step: Move either one step or 2 steps
    return climbStairs(n - 1) + climbStairs(n - 2)


if __name__ == '__main__':
    n = 2
    result = climbStairs(n)
    print(result)
