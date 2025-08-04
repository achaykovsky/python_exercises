from collections import deque


class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        if self.empty():
            raise IndexError("Pop from an empty stack")

        # Move all elements except the last to queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        # The last element in queue1 is the top of the stack
        popped_item = self.queue1.popleft()

        # swapping ensures that queue1 always contains the elements
        # in the correct stack order for subsequent operations.
        self.queue1, self.queue2 = self.queue2, self.queue1

        return popped_item

    def top(self) -> int:
        if self.empty():
            raise IndexError("Top from an empty stack")

        # Move all elements except the last to queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        # The last element in queue1 is the top of the stack
        top_item = self.queue1.popleft()
        self.queue2.append(top_item)  # Put it back in queue2

        # swapping ensures that queue1 always contains the elements
        # in the correct stack order for subsequent operations.
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_item

    def empty(self) -> bool:
        return len(self.queue1) == 0


if __name__ == '__main__':
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    myStack.top()
    myStack.pop()
    myStack.empty()
