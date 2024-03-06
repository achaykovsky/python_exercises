def sortSentence(s: str) -> str:
    words_list_from_sentence = s.split(" ")
    length = len(words_list_from_sentence)
    new_words_list = [None] * length

    for word in words_list_from_sentence:
        # get the index from the ending and shifting all the indices left by one
        index = int(word[-1]) - 1
        # get the word without the index number
        new_words_list[index] = word[:-1]

    result = " ".join(new_words_list)
    return result


if __name__ == '__main__':
    s = "is2 sentence4 This1 a3"
    result = sortSentence(s)
    print(result)
