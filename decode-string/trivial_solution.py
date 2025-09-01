# Time Complexity: O(n)
# Space Complexity: O(n)

def decodeString(s: str) -> str:
    stack = []

    for i in range(len(s)):
        if s[i] != ']':
            stack.append(s[i])
        else:
            sub_string = ""
            while stack[-1] != '[':  # new substring
                # we add the current letter with the substring (the addition order matters!!!)
                # NOTE: the addition order matters!!! - (stack.pop() + sub_string) and (sub_string + stack.pop())  are different!!
                sub_string = stack.pop() + sub_string
            stack.pop()  # remove the '[' we just finished to compute

            k = ""  # the number we calculate to multiply our string
            while stack and stack[-1].isdigit():
                # we add the current digit with the substring
                # NOTE: the addition order matters!!! - (stack.pop() + k) and (k + stack.pop())  are different!!
                k = stack.pop() + k

            stack.append(int(k) * sub_string)

    return "".join(stack)


if __name__ == '__main__':
    s = "3[a]2[bc]"
    result = decodeString(s)
    print(result)
