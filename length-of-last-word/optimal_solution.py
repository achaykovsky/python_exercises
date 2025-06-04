# Time Complexity: O(n)
# Space Complexity:O(1)

def lengthOfLastWord(s: str) -> int:
    length = len(s) - 1
    counter = 0

    while s[length] == " ":  # skipping all the spaces in the end
        length -= 1

    while s[length] != " " and length >= 0:  # counting the last word
        length -= 1
        counter += 1

    return counter


if __name__ == '__main__':
    s = "hi     Anna "
    result = lengthOfLastWord(s)
    print(result)
