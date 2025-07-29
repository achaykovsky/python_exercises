from collections import deque


# LeetCode instructions: You must use only standard operations of a queue,
# which means that only push to back, peek/pop from front, size and is empty operations are valid
# which means that pop which is used in this solution is NOT allowed
# also peeking from the end (self.queue[-1]), is NOT allowed in a regular queue

# we use here deque - which is a double ended queue, that have options that we aren't allowed to use

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.empty():
            return self.queue.pop()  # removing the last
        raise IndexError("Can't top from an empty stack")

    def top(self) -> int:
        if not self.empty():
            item = self.queue[-1]
            return item
        raise IndexError("Can't top from an empty stack")

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False


if __name__ == '__main__':
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    myStack.top()
    myStack.pop()
    myStack.empty()
