from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)
def jump(nums: List[int]) -> int:
    n = len(nums)
    result = 0  # Number of jumps
    end = 0  # End of current jump range
    farthest = 0  # Farthest index reachable in current range

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        if i == end:  # we've reached the boundary of the current jump
            result += 1  # increment number of jumps
            end = farthest  # start a new range

    return result


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    result = jump(nums)
    print(result)
