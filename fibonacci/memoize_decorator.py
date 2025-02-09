import functools


# Time complexity: O(n)
# Space Complexity: O(n)
def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Returning cached result: {cache[args]}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@memoize
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(100))  # Uses caching
