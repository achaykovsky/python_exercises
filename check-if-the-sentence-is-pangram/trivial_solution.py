# This is a generic file for the trivial solution
from collections import Counter


def checkIfPangram(sentence: str) -> bool:
    freq_hash = Counter(sentence)
    if len(freq_hash.keys()) == 26:
        return True
    return False


if __name__ == '__main__':
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    result = checkIfPangram(sentence)
    print(result)
