# This is a generic file for the trivial solution

def isValid(s: str) -> bool:
    stack = []
    bracket_types = {'(': ')', '[': ']', '{': '}'}

    for bracket in s:
        if bracket in bracket_types:
            stack.append(bracket)
        # if len of the stack is zero, but we still have a bracket, it means it doesn't have a pair
        # if type of the bracket we get is different from the closing type, it means we can't close it
        elif len(stack) == 0 or bracket != bracket_types[stack.pop()]:
            return False

    return len(stack) == 0


if __name__ == '__main__':
    s = "(){}"
    result = isValid(s)
    print(result)
