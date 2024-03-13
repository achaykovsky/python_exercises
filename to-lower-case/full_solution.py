LETTERS_DIFF = (ord('A') - ord('a'))


def toLowerCase(s: str) -> str:
    result = ""
    for c in s:
        if not c.islower():
            c_lower = chr(ord(c) - LETTERS_DIFF)
            result += c_lower
        else:
            result += c
    return result


if __name__ == '__main__':
    s = "Hello"
    result = toLowerCase(s)
    print(result)
