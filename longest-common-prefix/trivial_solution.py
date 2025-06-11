from typing import List


# Time Complexity: O(n * m) where n is the number of strings and m is the length of the shortest string
# Space Complexity: O(1)
def longestCommonPrefix(strs: List[str]) -> str:
    result = ""
    if not strs:
        return result

    # finding the shortest word, which will be the max of the longest prefix
    min_word = min(strs, key=len)

    # looping through this shortest word to find the longest prefix in the words list
    for i in range(len(min_word)):
        for s in strs:
            if s[i] != min_word[i]:
                return result
        result += min_word[i]

    return result


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    result = longestCommonPrefix(strs)
    print(result)
