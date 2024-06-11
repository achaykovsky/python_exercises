from math import ceil


# Time complexity: O(n), Space Complexity: O(n)
def encrypt(word):
    result = []
    UPPER_BOUND = ord("z")  # 122

    for c in word:
        result.append(ord(c))

    for i, c in enumerate(result, start=1):
        if i == 0:
            result[i] += 1
        if i < len(word):
            result[i] = result[i] + result[i - 1]

    for i, c in enumerate(result):
        differnece = c - UPPER_BOUND
        number_of_multiplication = ceil(differnece / 26)
        new_diff = number_of_multiplication * 26 - differnece
        result[i] = chr(UPPER_BOUND - new_diff + 1)

    return "".join(result)


if __name__ == '__main__':
    solution_input = "crime"
    result = encrypt(solution_input)
    print(result)
