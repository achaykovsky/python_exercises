def checkIfPangram(sentence: str) -> bool:
    panagram = set(sentence)
    return len(panagram) == 26


if __name__ == '__main__':
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    result = checkIfPangram(sentence)
    print(result)
