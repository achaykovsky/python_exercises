# Time Complexity: O(2^(m+n))
# Space Complexity: O(m+n) - for the recursion stack
def uniquePaths(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1
    return uniquePaths(m - 1, n) + uniquePaths(m, n - 1)


if __name__ == '__main__':
    m = 3
    n = 7
    result = uniquePaths(m, n)
    print(result)
