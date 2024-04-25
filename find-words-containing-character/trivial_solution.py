from typing import List


def findWordsContaining(words: List[str], x: str) -> List[int]:
    result = []
    for i, word in enumerate(words):
        if x in word:
            result.append(i)
    return result


if __name__ == '__main__':
    words, x = ["leet", "code"], "e"
    result = findWordsContaining(words, x)
    print(result)
