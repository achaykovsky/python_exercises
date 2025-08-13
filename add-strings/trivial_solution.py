# Time Complexity: O(max(len1, len2)))
# Space Complexity: O(max(len1, len2)))
def addStrings(num1: str, num2: str) -> str:
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    res = []
    while i >= 0 or j >= 0 or carry:
        # create the digit (d1) from num1
        if i >= 0:
            d1 = int(num1[i])
        else:
            d1 = 0

        # create the digit (d2) from num2
        if j >= 0:
            d2 = int(num2[j])
        else:
            d2 = 0

        total = d1 + d2 + carry

        curr_digit = str(total % 10)
        res.append(curr_digit)

        carry = total // 10

        i -= 1
        j -= 1

    return "".join(reversed(res))


if __name__ == '__main__':
    num1 = "11"
    num2 = "123"
    result = addStrings(num1, num2)
    print(result)
