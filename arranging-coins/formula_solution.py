import math
# Using the arithmetic series formula -> from the binary search solution
#   coins_needed = k * (k + 1) / 2

# Step 2: Set up inequality
# We want the largest k such that:
#   k * (k + 1) / 2 <= n

# Step 3: Rearrange into quadratic form
#   k^2 + k - 2n <= 0

# Step 4: Solve quadratic using formula
#   k = (-1 ± sqrt(1 + 8n)) / 2

# Step 5: Choose the positive root
#   k = (-1 + sqrt(1 + 8n)) / 2

# Step 6: Take floor (since we need an integer number of rows)
#   k = floor((-1 + sqrt(1 + 8n)) / 2)

# Final Formula:
#   k = floor((math.isqrt(1 + 8*n) - 1) / 2)

# Time Complexity: O(1)
# Space Complexity: O(1)
def arrangeCoins(n: int) -> int:
    # isqrt function avoids the rounding issues that floor/ceil could break
    # works safely for big numbers
    return int((math.isqrt(1 + 8 * n) - 1) // 2)


if __name__ == '__main__':
    n = 5
    result = arrangeCoins(n)
    print(result)
