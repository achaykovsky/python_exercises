def halvesAreAlike(s: str) -> bool:
    lowercase_vowels_first_half = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    uppercase_vowels_first_half = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
    lowercase_vowels_second_half = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    uppercase_vowels_second_half = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
    half_pos = int(len(s) / 2) - 1
    start_range, end_range = 0, half_pos
    update_vowel_instances(s, start_range, end_range, lowercase_vowels_first_half, uppercase_vowels_first_half)
    start_range, end_range = half_pos + 1, len(s) - 1
    update_vowel_instances(s, start_range, end_range, lowercase_vowels_second_half, uppercase_vowels_second_half)

    first_half = sum(lowercase_vowels_first_half.values()) + sum(uppercase_vowels_first_half.values())
    second_half = sum(lowercase_vowels_second_half.values()) + sum(uppercase_vowels_second_half.values())

    if first_half == second_half:
        return True

    return False


def update_vowel_instances(s, start_range, end_range, lowercase_vowels_dict, uppercase_vowels_dict):
    for i in range(start_range, end_range + 1):
        c = s[i]
        if c in lowercase_vowels_dict.keys():
            lowercase_vowels_dict[c] += 1
        elif c in uppercase_vowels_dict.keys():
            uppercase_vowels_dict[c] += 1


if __name__ == '__main__':
    s = "textbook"
    result = halvesAreAlike(s)
    print(result)
