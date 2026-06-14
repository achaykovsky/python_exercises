from typing import List


# Time Complexity: O(n)
# Space Complexity: O(n)
def fizzBuzz(n: int) -> List[str]:
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


if __name__ == '__main__':
    n = 5
    result = fizzBuzz(n)
    print(result)
