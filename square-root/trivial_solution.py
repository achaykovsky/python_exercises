# This is a generic file for the trivial solution

def mySqrt(x: int) -> int:
    base = 1

    while pow(base, 2) < x:
        base += 1

    if pow(base, 2) > x:
        base -= 1

    return base


if __name__ == '__main__':
    x = 16
    result = mySqrt(x)
    print(result)
