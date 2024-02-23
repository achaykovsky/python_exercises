# This is a generic file for the trivial solution

def balancedStringSplit(s):
    result = 0
    r, l = 0, 0
    for c in s:
        match c:
            case 'R':
                r += 1
            case 'L':
                l += 1
        if (r == l) and (r != 0):
            result += 1
            r, l = 0, 0

    return result


if __name__ == '__main__':
    s = "RLRRRLLRLL"
    result = balancedStringSplit(s)
    print(result)
