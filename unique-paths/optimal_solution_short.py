# Time Complexity: O(m * n)
# Space Complexity: O(n) - we only need to keep track of one row at a time
def uniquePaths(m: int, n: int) -> int:
    row = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            row[j] += row[j - 1]  # sum the paths from the left and above
    return row[-1]


if __name__ == '__main__':
    m = 3
    n = 7
    result = uniquePaths(m, n)
    print(result)
