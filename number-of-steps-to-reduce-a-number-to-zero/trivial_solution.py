def numberOfSteps(num: int) -> int:
    result = 0

    while (num != 0):
        if num % 2 == 0:
            num = num // 2
        else:
            num -= 1
        result += 1
    return result


if __name__ == '__main__':
    num = 14
    result = numberOfSteps(num)
    print(result)
