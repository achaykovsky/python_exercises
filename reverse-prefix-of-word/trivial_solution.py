def reversePrefix(word: str, ch: str) -> str:
    first_index = word.find(ch)
    string_to_reverse = word[:first_index + 1]  # adding one to include the ch
    reversed_prefix = string_to_reverse[::-1]
    result = reversed_prefix + word[first_index + 1:]  # adding one to exclude the ch
    return result


if __name__ == '__main__':
    word = "abcdefd"
    ch = "d"
    result = reversePrefix(word, ch)
    print(result)
