# This is a generic file for the trivial solution

# Time complexity: O(n)
# Space complexity: O(n)

# decryption function: dec[n] = enc[n] - secondStep[n-1] + 26m
def decrypt(word):
    length = len(word)
    decryption = ""
    second_step = 1

    for i in range(length):
        ascii_rep = ord(word[i])  # enc[n]
        ascii_rep -= second_step  # enc[n] - secondStep[n-1]

        while ascii_rep < ord('a'):  # looking for the first instance it is above 'a', so it will be a letter
            ascii_rep += 26  # Going to be m loops to find it

        decryption += chr(ascii_rep)
        second_step += ascii_rep  # creating secondStep[n-1]

    return decryption


if __name__ == '__main__':
    solution_input = "dnotq"
    result = decrypt(solution_input)
    print(result)
