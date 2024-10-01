from typing import List


def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    full_string1, full_string2 = "", ""
    for word in word1:
        full_string1 += word

    for word in word2:
        full_string2 += word

    return full_string1 == full_string2


if __name__ == '__main__':
    word1, word2 = ["ab", "c"], ["a", "cb"]
    result = arrayStringsAreEqual(word1, word2)
    print(result)
