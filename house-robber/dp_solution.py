from typing import List


# This is the dp solution to the House Robber problem.

# Time Complexity: O(2^n)
# Space Complexity: O(n)
def rob(houses: List[int]) -> int:
    if not houses:
        return 0

    n = len(houses)
    if n == 1:
        return houses[0]

    # Create a dp array to store the maximum amount robbed up to each house
    dp = [0] * n
    # Base Case: when there's only one house, rob it

    dp[0] = houses[0]

    # Base Case: when there are two houses, rob the one with the maximum value
    dp[1] = max(houses[0], houses[1])

    # Fill the dp array using the recurrence relation
    for i in range(2, n):
        # Either rob the current house and add it to the amount robbed two houses back,
        # or skip the current house and take the amount robbed from the previous house.
        dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])

    return dp[-1]


if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]
    result = rob(nums)
    print(result)
