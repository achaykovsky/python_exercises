from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)
def rob(houses: List[int]) -> int:
    n = len(houses)
    if n == 0:  # No houses to rob
        return 0
    if n == 1:  # Only one house to rob
        return houses[0]
    if n == 2:  # Two houses to rob, take the maximum
        return max(houses[0], houses[1])

    # Sliding Two pointer technique to keep track of the maximum amount robbed
    prev2 = houses[0]  # First house
    prev1 = max(houses[0], houses[1])  # First two houses

    for i in range(2, n):
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        current = max(prev1, prev2 + houses[i])  # Rob current house and add to prev2

        # Update the previous values for the next iteration
        # prev2 = dp[i - 2] -> moves to dp[i - 1]
        # prev1 = dp[i - 1] -> moves to dp[i]
        prev2, prev1 = prev1, current

    # The last computed value is the maximum amount that can be robbed which will be in prev1
    return prev1


if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]
    result = rob(nums)
    print(result)
