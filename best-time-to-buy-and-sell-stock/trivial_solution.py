# This is a generic file for the trivial solution
from typing import List

# Time Complexity: O(n^2)
# Space Complexity: O(n)
def maxProfit(prices: List[int]) -> int:
    maximum_list = []
    for i, price in enumerate(prices):
        maximum_rest_array = max(prices[i:])
        diff = maximum_rest_array - price
        if diff > 0:
            maximum_list.append(diff)

    if len(maximum_list):
        result = max(maximum_list)
    else:
        return 0
    return result


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    # prices = [7, 6, 4, 3, 1]
    result = maxProfit(prices)
    print(result)
