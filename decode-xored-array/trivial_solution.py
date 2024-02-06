# This is a generic file for the trivial solution
from typing import List


# encoded[i] = arr[i] ^ arr[i + 1]
def solution(encoded: List[int], first: int):
    result = [first]
    index = 0
    for encoded_element in encoded:
        decoded = encoded_element ^ result[index]
        result.append(decoded)
        index += 1
    return result


if __name__ == '__main__':
    encoded = [1, 2, 3]
    first = 1
    result = solution(encoded, first)
    print(result)
