def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    result = address.replace('.', '[.]')
    return result


if __name__ == '__main__':
    address = "255.100.50.0"
    result = defangIPaddr(address)
    print(result)
