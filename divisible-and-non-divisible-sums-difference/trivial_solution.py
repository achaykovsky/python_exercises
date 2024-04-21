def differenceOfSums(n: int, m: int) -> int:
    divisble = []
    non_divisble = []
    for i in range(1, n + 1):
        if i % m == 0:
            divisble.append(i)
        else:
            non_divisble.append(i)

    num1 = sum(non_divisble)
    num2 = sum(divisble)

    return num1 - num2


if __name__ == '__main__':
    n, m = 10, 3
    result = differenceOfSums(n, m)
    print(result)
