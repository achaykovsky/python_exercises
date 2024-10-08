numbers_dict = {"10#": "j", "11#": "k", "12#": "l", "13#": "m", "14#": "n", "15#": "o", "16#": "p", "17#": "q",
                "18#": "r", "19#": "s", "20#": "t", "21#": "u", "22#": "v", "23#": "w", "24#": "x", "25#": "y",
                "26#": "z"}

digits_dict = {"1": "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f", "7": "g", "8": "h",
               "9": "i"}


def freqAlphabets(s: str) -> str:
    for number in numbers_dict:
        s = s.replace(number, numbers_dict[number])

    for digit in digits_dict:
        s = s.replace(digit, digits_dict[digit])

    return s


if __name__ == '__main__':
    s = "10#11#12"
    result = freqAlphabets(s)
    print(result)
