def triple_step(n: int) -> int:
    def triple(n, counter):
        if n < 0:
            return 0
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4

        counter += triple(n - 1, counter)
        counter += triple(n - 2, counter)
        counter += triple(n - 3, counter)

        return counter

    return triple(n, 0)


if __name__ == '__main__':
    n = 5
    result = triple_step(n)
    print(result)
