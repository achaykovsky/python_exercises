# This is a generic file for the trivial solution

# Time complexity: O(2^n) Space Complexity: O(n)
def fibonacci(n: int) -> int:
    if n <= 1:
        return n

    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    n = 5
    result = fibonacci(n)
    print(result)
