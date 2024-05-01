# This is a generic file for the trivial solution

def solution(numbers):
    zero_counter = 0
    result = []
    for i in numbers:
        if i != 0:
            result.append(i)
        else:
            zero_counter += 1

    for i in range(zero_counter):
        result.append(0)

    return result


if __name__ == '__main__':
    numbers = [0, 1, 0, 3, 12]
    result = solution(numbers)
    print(result)
