def removeOuterParentheses(s: str) -> str:
    counter = 0
    result = ""
    for c in s:
        if c == '(':
            counter += 1
            if counter > 1:
                result += '('
        elif c == ')':
            counter -= 1
            if counter >= 1:
                result += ')'
    return result


if __name__ == '__main__':
    s = "(()())(())"
    result = removeOuterParentheses(s)
    print(result)
