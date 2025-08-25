from typing import List


# Trivial solution for the Candy problem
# Time Complexity: O(n^2) in worst case
# Space Complexity: O(n)
def candy(ratings: List[int]) -> int:
    n = len(ratings)
    if n == 0:
        return 0

    # Initialize each child with 1 candy
    candies = [1] * n

    # Keep updating until no changes are made
    changed = True
    while changed:
        changed = False

        # Check all positions for violations
        for i in range(n):
            # Check left neighbor
            if i > 0 and ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                candies[i] = candies[i - 1] + 1
                changed = True

            # Check right neighbor
            if i < n - 1 and ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
                changed = True

    return sum(candies)


if __name__ == '__main__':
    ratings = [1, 0, 2]
    result = candy(ratings)
    print(result)
