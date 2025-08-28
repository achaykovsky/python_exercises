# Time Complexity: O(n+m)
# Space Complexity:O(n+m)
def backspaceCompare(s: str, t: str) -> bool:
    def build(string: str) -> list[str]:
        stack = []
        for char in string:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return stack

    return build(s) == build(t)


if __name__ == '__main__':
    s = "ab##"
    t = "c#d#"
    result = backspaceCompare(s, t)
    print(result)
