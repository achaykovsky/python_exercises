def finalValueAfterOperations(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    x = 0
    for i in operations:
        if i == "--X" or i == "X--":
            x -= 1
        else:
            x += 1
    return x


if __name__ == '__main__':
    operations = ["--X", "X++", "X++"]
    result = finalValueAfterOperations(operations)
    print(result)
