def triple_step(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1

    return triple_step(n - 1) + triple_step(n - 2) + triple_step(n - 3)


if __name__ == '__main__':
    n = 25
    result = triple_step(n)
    print(result)
