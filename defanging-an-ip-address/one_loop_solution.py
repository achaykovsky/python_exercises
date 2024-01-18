def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    result = []
    for i in address:
        if i == '.':
            result.append('[.]')
        else:
            result.append(i)
    ip_result = "".join(result)
    return ip_result


if __name__ == '__main__':
    address = "1.1.1.1"
    result = defangIPaddr(address)
    print(result)
