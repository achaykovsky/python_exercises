# Time Complexity: O(n) for push, O(1) for pop/peek/empty
# Space Complexity: O(n) for recursion stack (in push)
class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
            return

        temp = self.stack.pop()
        self.push(x)
        self.stack.append(temp)

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        val = self.stack.pop()
        self.stack.append(val)
        return val

    def empty(self) -> bool:
        return len(self.stack) == 0


if __name__ == '__main__':
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    myQueue.peek()
    myQueue.pop()
    myQueue.empty()
