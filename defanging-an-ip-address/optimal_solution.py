def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    result = ""
    for i in address:
        if i == '.':
            result += '[.]'
        else:
            result += i
    return result


if __name__ == '__main__':
    address = "1.1.1.1"
    result = defangIPaddr(address)
    print(result)
