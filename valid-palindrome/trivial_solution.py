def isPalindrome(s: str) -> bool:
    alphanumeric_s = ""

    alphanumeric_s = remove_non_alphanumeric_chars(alphanumeric_s, s)
    reversed_s = alphanumeric_s[::-1]  # reversing, but allocating extra space

    return reversed_s == alphanumeric_s


def remove_non_alphanumeric_chars(new_s, s):
    for c in s:
        if c.isalpha():
            new_s += c.lower()
        if c.isdigit():
            new_s += c.lower()

    return new_s


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    result = isPalindrome(s)
    print(result)
