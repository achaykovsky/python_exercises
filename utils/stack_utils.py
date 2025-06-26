# Stack implementation using a list in Python

class Stack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.size += 1

    def pop(self) -> int:
        if not self.is_empty():
            self.size -= 1
            return self.stack.pop()  # removing the last
        raise IndexError("Can't pop from an empty stack")

    def top(self) -> int:
        if not self.is_empty():
            item = self.stack[-1]
            return item
        raise IndexError("Can't top from an empty stack")

    def is_empty(self) -> bool:
        return self.size == 0
