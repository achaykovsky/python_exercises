# buttom-up dynamic programming approach to find the length of the longest common subsequence (LCS)

# Time Complexity: O(m * n) where m is the length of text1 and n is the length of text2
# Space Complexity: O(n) # for the DP table (optimized space)

def longestCommonSubsequence(text1: str, text2: str) -> int:
    if not text1 or not text2:
        return 0

    m, n = len(text1), len(text2)
    prev_row = [0] * (n + 1)

    for i in range(m - 1, -1, -1):

        curr_row = [0] * (n + 1)

        for j in range(n - 1, -1, -1):
            # If characters match, increment the count from
            # the previous diagonal cell which represents the LCS length for the remaining substrings
            if text1[i] == text2[j]:
                curr_row[j] = 1 + prev_row[j + 1]
            else:
                # If characters do not match, the LCS length at curr_row[j] can be found:
                # either by ignoring the current character of s1 or s2
                # - prev_row[j] means ignoring the current character of s1
                # - curr_row[j + 1] means ignoring the current character of s2
                curr_row[j] = max(prev_row[j], curr_row[j + 1])

        # Move to the next row, so we can use curr_row as prev_row in the next iteration
        prev_row = curr_row

    return prev_row[0]


if __name__ == '__main__':
    s1 = "abcde"
    s2 = "ace"
    result = longestCommonSubsequence(s1, s2)
    print(result)
