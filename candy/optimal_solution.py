from typing import List


# Optimal solution for the Candy problem using a two-pass greedy approach.
# Time Complexity: O(n)
# Space Complexity: O(n)
def candy(ratings: List[int]) -> int:
    n = len(ratings)
    if n <= 1:
        return n
    candies = [1] * n

    # First pass: left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Second pass: right to left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    return sum(candies)


if __name__ == '__main__':
    ratings = [1, 0, 2]
    result = candy(ratings)
    print(result)
