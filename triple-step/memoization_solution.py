from collections import defaultdict


def triple_step(n: int) -> int:
    memo = defaultdict(lambda: -1)

    def triple(n, memo):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if memo[n] != -1:
            return memo[n]

        return triple(n - 1, memo) + triple(n - 2, memo) + triple(n - 3, memo)

    return triple(n, memo)


if __name__ == '__main__':
    n = 5
    result = triple_step(n)
    print(result)
