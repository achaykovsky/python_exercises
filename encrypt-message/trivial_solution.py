from math import ceil


# Time complexity: O(n), Space Complexity: O(n)

# encryption function: enc[n] = dec[n] + secondStep[n-1] - 26m
def encrypt(word):
    result = []
    UPPER_BOUND = ord("z")

    for c in word:
        result.append(ord(c))

    for i, c in enumerate(result, start=1):
        if i == 0:
            result[i] = 1  # first letter
        if i < len(word):
            result[i] = result[i] + result[i - 1]  # rest of the letters

    for i, c in enumerate(result):
        difference = c - UPPER_BOUND
        number_of_multiplication = ceil(difference / 26)
        new_diff = number_of_multiplication * 26 - difference
        result[i] = chr(UPPER_BOUND - new_diff + 1)

    return "".join(result)


if __name__ == '__main__':
    solution_input = "crime"
    result = encrypt(solution_input)
    print(result)
