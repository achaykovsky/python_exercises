# This is a generic file for the trivial solution


# Time Complexity: O(m*n)
# Space Complexity: O(m)
def isSubsequence(s: str, t: str) -> bool:
    s = list(s)
    res = []

    for c in s:
        if c in t:
            res.append(c)

    return res == s


if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    result = isSubsequence(s, t)
    print(result)
