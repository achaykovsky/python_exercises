def replaceDigits(s: str) -> str:
    result = []
    for i in range(0, len(s), 2):
        result.append(s[i])
        if i + 1 < len(s):
            steps = int(s[i + 1])
            next_char = chr(ord(s[i]) + steps)
            result.append(next_char)
    return "".join(result)


if __name__ == '__main__':
    s = "a1b2c3d4e"
    result = replaceDigits(s)
    print(result)
