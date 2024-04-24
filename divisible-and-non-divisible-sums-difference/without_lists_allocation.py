def differenceOfSums(n: int, m: int) -> int:
    num1, num2 = 0, 0
    for i in range(1, n + 1):
        if i % m == 0:
            num2 += i
        else:
            num1 += i

    return num1 - num2


if __name__ == '__main__':
    n, m = 10, 3
    result = differenceOfSums(n, m)
    print(result)
