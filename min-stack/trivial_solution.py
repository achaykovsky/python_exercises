class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if not self.is_empty():
            self.stack.pop()

    def top(self) -> int:
        if not self.is_empty():
            return self.stack[-1]
        return -1

    def getMin(self) -> int:
        if not self.is_empty():
            return min(self.stack)
        return -1

    def is_empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()
    minStack.pop()
    minStack.top()
    minStack.getMin()
