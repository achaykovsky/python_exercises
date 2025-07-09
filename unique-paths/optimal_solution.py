# Example (m=3, n=4):
# [1, 1, 1, 1]
# [1, 2, 3, 4]
# [1, 3, 6, 10]

# Time Complexity: O(m * n)
# Space Complexity: O(n) - we only need to keep track of one row at a time
def uniquePaths(m: int, n: int) -> int:
    prev_row = [1] * n  # Initialize the first prev_row with 1s

    for r in range(1, m):  # Iterate through each prev_row starting from the second
        curr_row = [1] * n
        for c in range(1, n):
            curr_row[c] = curr_row[c - 1] + prev_row[c]
        prev_row = curr_row
    return prev_row[n - 1]  # The last element in the prev_row will be the answer


if __name__ == '__main__':
    m = 3
    n = 7
    result = uniquePaths(m, n)
    print(result)
