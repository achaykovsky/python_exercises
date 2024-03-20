from typing import List


def countConsistentStrings(allowed: str, words: List[str]) -> int:
    result = 0
    allowed_letters = set(allowed)

    for word in words:
        word_letters = set(word)
        if word_letters <= allowed_letters:
            result += 1

    return result


if __name__ == '__main__':
    allowed = "cad"
    words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
    result = countConsistentStrings(allowed, words)
    print(result)
