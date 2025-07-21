from typing import List


# Time complexity: O(m) m=amount
# Space Complexity: O(m)

# DP - bottom up
def coinChange(coins: List[int], amount: int) -> float:
    dp = [float('inf')] * (amount + 1)  # dp[i] = min number of coins to make amount i
    dp[0] = 0

    for coin in coins:
        for curr_amount in range(coin, amount + 1):
            dp[curr_amount] = min(dp[curr_amount], 1 + dp[
                curr_amount - coin])  # 1 + dp[curr_amount - coin] means using one more coin of type coin

    if dp[amount] == float('inf'):  # amount cannot be made up by any combination of coins
        return -1

    return dp[amount]  # return the minimum number of coins needed to make up the amount


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(coinChange(coins, amount))
    # Output: 3 (11 = 5 + 5 + 1)
