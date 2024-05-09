def isPalindrome(s: str) -> bool:
    length = len(s) - 1

    for c in s:
        if c.isspace() or not c.isalnum():
            continue
        while s[length].isspace() or not s[length].isalnum():
            length -= 1

        if c.lower() != s[length].lower():
            return False
        else:
            length -= 1
    return True


if __name__ == '__main__':
    s = "race a car"
    # s = "A man, a plan, a canal: Panama"
    result = isPalindrome(s)
    print(result)
