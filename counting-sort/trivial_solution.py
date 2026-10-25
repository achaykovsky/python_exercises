# Counting Sort Implementation
# Time Complexity: O(n + k) where n is the number of elements in the input array and k is the range of the input values.
# Space Complexity: O(k) for the counts array
def CountingSort(nums: list[int]) -> list[int]:
    if not nums:
        return []
    counts = [0] * (max(nums) + 1)
    result = []

    for num in nums:  # O(n)
        counts[num] += 1

    for i, count in enumerate(counts):  # O(k)
        result.extend([i] * count)

    return result


if __name__ == '__main__':
    nums = [4, 2, 2, 8, 3, 3, 1]
    result = CountingSort(nums)
    print(result)
