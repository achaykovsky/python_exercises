def isPalindrome(s: str) -> bool:
    r, l = 0, len(s) - 1

    while r < l:
        while s[r].isspace() or not s[r].isalnum():  # validating the right char for alphanumeric and spaces
            r += 1
        while s[l].isspace() or not s[l].isalnum():  # validating the left char for alphanumeric and spaces
            l -= 1

        # failing if a mismatch was found
        if s[r].lower() != s[l].lower():
            return False

        l -= 1
        r += 1
    return True


if __name__ == '__main__':
    s = "race a car"
    # s = "A man, a plan, a canal: Panama"
    result = isPalindrome(s)
    print(result)
