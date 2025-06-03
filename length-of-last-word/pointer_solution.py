# Time Complexity: O(n)
# Space Complexity:O(1)

def lengthOfLastWord(s: str) -> int:
    length = len(s) - 1
    counter = 0

    while length >= 0:
        if s[length] == ' ' and counter == 0:
            length -= 1
            continue
        elif s[length] != ' ':
            length -= 1
            counter += 1
        elif s[length] == ' ' and counter != 0:
            break

    return counter


if __name__ == '__main__':
    s = "a"
    result = lengthOfLastWord(s)
    print(result)
