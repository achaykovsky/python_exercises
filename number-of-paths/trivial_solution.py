# recursion solution

# to make the base case 0,0 we need to start from the ending

# Time Complexity: O(2^n) Space: O(n)
def num_of_paths_to_dest(n):
    def calculate_path(i, j):
        if i < j or i < 0 or j < 0:  # if we pass the borders and violate the constraint it is not a valid path
            return 0

        # base case
        if i == 0 and j == 0:  # if we arrived to the start it is a valid path
            return 1

        return calculate_path(i, j - 1) + calculate_path(i - 1, j)  # sum the possible paths

    return calculate_path(n - 1, n - 1)  # start from the destination


if __name__ == '__main__':
    n = 1  # A: 1
    n = 2  # A: 1
    # n = 3  # A: 2
    n = 4  # A: 5
    n = 6  # A: 42
    n = 17  # A: 35357670
    result = num_of_paths_to_dest(n)
    print(result)
