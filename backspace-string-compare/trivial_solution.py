# Time Complexity: O(n)
# Space Complexity:O(n)

def backspaceCompare(s: str, t: str) -> bool:
    stack_s = fill_in_stack(s)
    stack_t = fill_in_stack(t)

    return stack_s == stack_t


def fill_in_stack(s):
    stack = []
    for c in s:
        if c != '#':
            stack.append(c)
        elif len(stack):
            stack.pop()
    return stack


if __name__ == '__main__':
    s = "ab##"
    t = "c#d#"
    result = backspaceCompare(s, t)
    print(result)
