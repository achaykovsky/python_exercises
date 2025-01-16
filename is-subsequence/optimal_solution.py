# This is a generic file for the trivial solution


# Time Complexity: O(m*n)
# Space Complexity: O(m)
def isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    if len(s) > len(t):
        return False

    while i < len(s) and j < len(t):
        if s[i] == t[j]:  # advancing for every found character
            i += 1
        j += 1

    return True if i == len(s) else False  # we finished all the letters on s subsequence -> True
    # else -> False


if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    result = isSubsequence(s, t)
    print(result)
