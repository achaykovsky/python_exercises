from typing import List


def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    full_string1 = "".join(word1)
    full_string2 = "".join(word2)
    return full_string1 == full_string2


if __name__ == '__main__':
    word1, word2 = ["ab", "c"], ["a", "cb"]
    result = arrayStringsAreEqual(word1, word2)
    print(result)
