from typing import List


# Time complexity: O(2^n)
# Space Complexity: O(n)

# recursive
def coinChange(coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    min_coins = float('inf')
    for coin in coins:
        res = coinChange(coins, amount - coin)
        if res != float('inf'):
            min_coins = min(min_coins, res + 1)

    return min_coins if min_coins != float('inf') else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(coinChange(coins, amount))
