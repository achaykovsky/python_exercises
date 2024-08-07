# T: O(n^3+nlogn) = O(n^3)
# S: O(1)
def find_array_quadruplet(arr, s):
    arr.sort()  # S: O(1) - in place
    result = []
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr) - 1):
            new_sum = s - (arr[i] + arr[j])
            l, r = j + 1, len(arr) - 1
            while (l < r):
                if arr[l] + arr[r] == new_sum:
                    return [arr[i], arr[j], arr[l], arr[r]]
                elif arr[l] + arr[r] > new_sum:
                    r -= 1
                else:
                    l += 1

    return result
