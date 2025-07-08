# Example (m=3, n=4):
# [1, 1, 1, 1]
# [1, 2, 3, 4]
# [1, 3, 6, 10]


# Dynamic Programming Solution

# Time Complexity: O(m * n)
# Space Complexity: O(n) - we only need to keep track of one row at a time
def uniquePaths(m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)]  # Initialize a 2D dp array with 1s
    for r in range(1, m):
        for c in range(1, n):
            # The number of unique paths to (r, c)
            # is the sum of paths from the cell above (r-1, c)
            # and the cell to the left (r, c-1)
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
    return dp[m - 1][n - 1]  # The bottom-right corner will have the answer


if __name__ == '__main__':
    m = 3
    n = 7
    result = uniquePaths(m, n)
    print(result)
