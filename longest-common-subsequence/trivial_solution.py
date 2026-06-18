# Time Complexity: O(2^(m+n)) where m is the length of s1 and n is the length of s2
# Space Complexity: O(m + n) for the recursion stack
def longestCommonSubsequence(s1: str, s2: str) -> int:
    def lcs(i: int, j: int) -> int:
        if i == len(s1) or j == len(s2):
            return 0

        if s1[i] == s2[j]:
            return 1 + lcs(i + 1, j + 1)
        else:
            return max(lcs(i + 1, j), lcs(i, j + 1))

    return lcs(0, 0)


if __name__ == '__main__':
    s1 = "abcde"
    s2 = "ace"
    result = longestCommonSubsequence(s1, s2)
    print(result)
