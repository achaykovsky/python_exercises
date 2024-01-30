def solution(command):
    result = ''
    for i, char in enumerate(command):
        if char == 'G':
            result += 'G'
        elif char == '(' and command[i + 1] == ')':
            result += 'o'
        elif char == '(' and command[i + 1] == 'a':
            result += 'al'

    return result


if __name__ == '__main__':
    command = "(al)G(al)()()G"
    result = solution(command)
    print(result)
