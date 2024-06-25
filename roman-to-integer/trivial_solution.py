romans_to_ints = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def romanToInt(s: str) -> int:
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and romans_to_ints[s[i]] < romans_to_ints[s[i + 1]]:
            result -= romans_to_ints[s[i]]
        else:
            result += romans_to_ints[s[i]]

    return result


if __name__ == '__main__':
    s = "MCMXCIV"
    result = romanToInt(s)
    print(result)
