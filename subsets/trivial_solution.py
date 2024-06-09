def subsets(nums):
    res = []
    subset = []

    def dfs(start):
        if start >= len(nums):
            res.append(subset.copy())
            return

        # include nums[i]
        subset.append(nums[start])
        dfs(start + 1)

        # do not include nums[i]
        subset.pop()  # remove nums[i]
        dfs(start + 1)

    dfs(0)
    return res


if __name__ == '__main__':
    solution_input = [1, 2, 3]
    result = subsets(solution_input)
    print(result)
