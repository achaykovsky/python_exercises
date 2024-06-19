# Memoization solution
from collections import defaultdict


# Time Complexity: O(n^2) Space: O(n^2)
def num_of_paths_to_dest(n):
    memo = defaultdict(lambda: defaultdict(lambda: -1))  # initializing a memo with -1 in every cell

    def calculate_path(i, j, memo):
        if i < 0 or j < 0:  # 1. out of the borders
            return 0
        elif i < j:  # 2. found an impossible cell. No path can be here. mark 0
            memo[i][j] = 0
        elif memo[i][j] != -1:  # 3. a cell we have calculated the number of paths for it
            return memo[i][j]
        elif i == 0 and j == 0:  # 4. reached the base case ---> found a path
            memo[i][j] = 1
        else:  # 5. 0<i<n-1 and 0<j<n-1 ---> we need to summarize the previous results
            memo[i][j] = calculate_path(i - 1, j, memo) + calculate_path(i, j - 1, memo)

        return memo[i][j]

    return calculate_path(n - 1, n - 1, memo)


if __name__ == '__main__':
    n = 1  # A: 1
    n = 2  # A: 1
    # n = 3  # A: 2
    n = 4  # A: 5
    # n = 6  # A: 42
    n = 17  # A: 35357670
    result = num_of_paths_to_dest(n)
    print(result)
