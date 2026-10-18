# The "Climbing Stairs" problem is a Fibonacci problem
# because the number of ways to reach step n.
# n depends directly on the ways to reach the two preceding steps, n-1 and n-2
# f(n) = f(n-1) + f(n-2)

# Time Complexity: O(n)
# Space Complexity: O(1)
def climbStairs(n: int) -> int:
    if n <= 2:
        return n

    # Base cases: # f(2) = 2, f(1) = 1
    one_step_before, two_steps_before = 2, 1
    for _ in range(3, n + 1):
        # Update to the next Fibonacci number
        curr = one_step_before + two_steps_before  # f(n) = f(n-1) + f(n-2)
        two_steps_before, one_step_before = one_step_before, curr  # Update the previous two steps

    return one_step_before


if __name__ == '__main__':
    n = 2
    result = climbStairs(n)
    print(result)
