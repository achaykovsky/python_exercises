# This is a generic file for the trivial solution


# Time complexity: O(logn) Space: O(1)
def root(x: int, n: int) -> float:
    l, r = 0, x
    result = 0

    while l <= r:
        m = (l + r) / 2
        if abs(x - pow(m, n)) <= 0.001:
            result = m
            break
        elif pow(m, n) > x:
            r = m
        else:
            l = m
    return round(result, 3)


if __name__ == '__main__':
    x = 0
    n = 3
    result = root(x, n)
    print(result)
