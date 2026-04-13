# Bottom-up Dynamic Programming Solution

# Time Complexity: O(n)
# Space Complexity: O(n)

def climbStairs(n: int) -> int:
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    # Base cases
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        # Calculate the number of ways to reach step i
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]  # Return the number of ways to reach the nth step


if __name__ == '__main__':
    n = 2
    result = climbStairs(n)
    print(result)
