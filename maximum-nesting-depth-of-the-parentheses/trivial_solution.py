def maxDepth(s: str) -> int:
    counter = 0
    nested_max = 0
    for c in s:
        match c:
            case '(':
                counter += 1
                nested_max = max(nested_max, counter)
            case ')':
                counter -= 1

    return nested_max


if __name__ == '__main__':
    s = "(1)+((2))+(((3)))"
    result = maxDepth(s)
    print(result)
