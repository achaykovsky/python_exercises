# The idea is that we have two stacks:
# One for popping - pop_stack
# One for pushing - push_stack

# To make it a Queue, meaning FIFO, we want the first numbers that we pushed into our queue, to be popped first.
# we pushed them into a stack, so they are the last, we need to put them first, to be able, to pop them first.
# so we reverse the whole stack of the push into the pop.


# Time Complexity: O(1) amortized per operation
# Space Complexity: O(n)
class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if len(self.pop_stack) == 0:
            while self.push_stack:
                # move all elements to pop_stack - so we will have the last elements we pushed first, when we pop
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self) -> int:
        if len(self.pop_stack) == 0:
            while self.push_stack:
                # move all elements to pop_stack - so we will have the last elements we pushed first, when we peek
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]

    def empty(self) -> bool:
        return len(self.push_stack) == 0 and len(self.pop_stack) == 0


if __name__ == '__main__':
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    myQueue.peek()
    myQueue.pop()
    myQueue.empty()
