from typing import List

# Time Complexity: O(n)
# Space Complexity: O(n)
def fizzBuzz(n: int) -> List[str]:
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result[i] = "FizzBuzz"
        elif i % 3 == 0:
            result[i] = "Fizz"
        elif i % 5 == 0:
            result[i] = "Buzz"
        else:
            result[i] = str(i)

    return result[1:]


if __name__ == '__main__':
    n = 5
    result = fizzBuzz(n)
    print(result)
