numbers_dict = {"10#": "j", "11#": "k", "12#": "l", "13#": "m", "14#": "n", "15#": "o", "16#": "p", "17#": "q",
                "18#": "r", "19#": "s", "20#": "t", "21#": "u", "22#": "v", "23#": "w", "24#": "x", "25#": "y",
                "26#": "z"}


def freqAlphabets(s: str) -> str:
    result = []
    i = 0
    length = len(s)
    while i <= length - 1:
        if i + 2 < length and s[i + 2] == '#':
            curr = s[i] + s[i + 1] + '#'  # can be updated to s[i:i + 3]
            sub_result = numbers_dict[curr]
            result.append(sub_result)
            i += 3
        else:
            single_digit = chr(ord('a') + int(s[i]) - 1)
            result.append(single_digit)
            i += 1

    return "".join(result)


if __name__ == '__main__':
    s = "10#11#12"
    result = freqAlphabets(s)
    print(result)
