# Time Complexity: O(n)
# Space Complexity:O(n)
def lengthOfLastWord(s: str) -> int:
    s = s.strip(" ").split(" ")
    return len(s[-1])


if __name__ == '__main__':
    s = "   fly me   to   the moon  "
    result = lengthOfLastWord(s)
    print(result)
