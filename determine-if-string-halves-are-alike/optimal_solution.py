vowels = ('a', 'e', 'i', 'o', 'u')


def halvesAreAlike(s: str) -> bool:
    first_half_counter, second_half_counter = 0, 0
    length = len(s)
    half_pos = length // 2
    for i in range(0, half_pos):
        if s[i].lower() in vowels:
            first_half_counter += 1
    for i in range(half_pos, length):
        if s[i].lower() in vowels:
            second_half_counter += 1

    return first_half_counter == second_half_counter


if __name__ == '__main__':
    s = "boek"
    result = halvesAreAlike(s)
    print(result)
