def calculatePair(a, b):
    return abs(ord(a) - ord(b))


def scoreOfString(s: str) -> int:
    sum, total_sum = 0, 0
    for i, c in enumerate(s):
        total_sum += sum
        if i + 1 < len(s):
            sum = calculatePair(c, s[i + 1])
    return total_sum


if __name__ == '__main__':
    s = "hello"
    result = scoreOfString(s)
    print(result)
