# Each number is evaluated with its sign (either + or -),
# and we treat subtraction as adding a negative number: -2 -> +(-2)
# We build the full number first
# When we encounter '(', we push the current result and sign onto the stack.
# We push the sign after the result so it will be popped first (LIFO),
# and apply it to the result of the parenthesized expression.


# Time Complexity: O(n)
# Space Complexity: O(n)

def calculate(s: str) -> int:
    stack = []
    current_num, sign = 0, 1
    result = 0

    for c in s:
        if c.isdigit():
            # construct the current number
            current_num = current_num * 10 + int(c)

        elif c in ('+', '-'):
            # calculating the current number based on the previous sign
            result += sign * current_num
            # decide the sign for the next number
            sign = 1 if c == '+' else -1
            current_num = 0

        elif c == '(':
            # push current result and the sign into the stack
            stack.append(result)
            stack.append(sign)
            # we need to start evaluate a new expression (the result already updated and processed on the stack)
            result, sign = 0, 1

        elif c == ')':
            # finished calculating the current bracket expression -> add to result
            result += sign * current_num
            # change the sign according to the sign before the bracket
            result *= stack.pop()
            # add the previous result
            result += stack.pop()

            current_num = 0

    # calculate the final number by adding the last number to the result
    result += current_num * sign
    return result


if __name__ == '__main__':
    s = "(1+7)"  # equals to +1+7
    result = calculate(s)
    print(result)
