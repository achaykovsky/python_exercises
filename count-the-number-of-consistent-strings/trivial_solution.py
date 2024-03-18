from typing import List


def countConsistentStrings(allowed: str, words: List[str]) -> int:
    allowed_letters = set(allowed)
    words_num = len(words)

    for word in words:
        for letter in word:
            if letter not in allowed_letters:
                words_num -= 1
                break

    return words_num


if __name__ == '__main__':
    allowed = "cad"
    words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
    result = countConsistentStrings(allowed, words)
    print(result)
