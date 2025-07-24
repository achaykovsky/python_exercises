from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)
def maxProfit(prices: List[int]) -> int:
    l, r = 0, 1  # left = buy, right = sell
    max_profit = 0

    for i in range(len(prices) - 1):
        if prices[l] < prices[r]:
            diff = prices[r] - prices[l]
            max_profit = max(diff, max_profit)
        elif prices[l] > prices[r]:
            l = r
        r += 1

    return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    # prices = [7, 6, 4, 3, 1]
    result = maxProfit(prices)
    print(result)
