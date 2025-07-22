from collections import deque
from typing import List


# Time complexity: O(m*n)
# Space Complexity: O(n)

# BFS
def coinChange(coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0

    queue = deque([(0, 0)])  # (current sum, number of coins used)
    visited = set()

    while queue:
        current_sum, steps = queue.popleft()  # Dequeue the first element

        for coin in coins:
            new_sum = current_sum + coin

            if new_sum == amount:  # Found a solution
                return steps + 1

            if new_sum < amount and new_sum not in visited:  # Avoid revisiting
                visited.add(new_sum)
                queue.append((new_sum, steps + 1))

    return -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(coinChange(coins, amount))
