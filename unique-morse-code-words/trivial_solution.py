from typing import List


def uniqueMorseRepresentations(words: List[str]) -> int:
    morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                  "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    translated_words = []
    for word in words:
        morse_word = []
        for letter in word:
            morse_word.append(morse_code[ord(letter) - ord('a')])
        translated_word = "".join(morse_word)
        translated_words.append(translated_word)

    result = len(set(translated_words))
    return result


if __name__ == '__main__':
    words = ["gin", "zen", "gig", "msg"]
    result = uniqueMorseRepresentations(words)
    print(result)
