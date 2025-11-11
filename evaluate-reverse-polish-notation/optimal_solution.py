from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)
def evalRPN(tokens: List[str]) -> int:
    stack = []

    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(token))

    return stack[0]


if __name__ == '__main__':
    tokens = ["2", "1", "+", "3", "*"]
    result = evalRPN(tokens)
    print(result)
