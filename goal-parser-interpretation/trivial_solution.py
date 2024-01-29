def solution(command):
    command = command.replace("()", "o").replace("(al)", "al")
    return command


if __name__ == '__main__':
    command = "(al)G(al)()()G"
    result = solution(command)
    print(result)
