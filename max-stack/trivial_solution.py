# The idea here is to have two stacks in the class.
# We push to the stack and pop from to both of them:
# 1. The general stack
# 2. The stack that has the max values.
# For each push operation, we will do a max operation between the last max and the current val and add the updated max the the max_values stack
# For each pop operation, we will pop from the top of the max_values stack as well.

class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_values = []

    def push(self, val: int) -> None:
        if not self.is_empty():
            self.max_values.append(max(val, self.max_values[-1]))  # add the new max to the max_values stack
        else:
            self.max_values.append(val)  # if the stack is empty, the first entry will be the max
        self.stack.append(val)  # add to the stack

    def pop(self) -> int:
        if not self.is_empty():  # pop from both of the stacks if the stack is not empty
            return self.stack.pop()
        return -1

    def top(self) -> int:
        if not self.is_empty():  # retrieve the value (peeking) - without poping it out
            return self.stack[-1]
        return -1

    def peekMax(self) -> int:
        if not self.is_empty():
            return self.max_values[-1]  # get the max value from the top of the max_values
        return -1

    def is_empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False


if __name__ == '__main__':
    maxStack = MaxStack()
    maxStack.push(-2)
    maxStack.push(0)
    maxStack.push(-3)
    print(maxStack.peekMax())
    maxStack.pop()
    maxStack.top()
    maxStack.push(5)
    maxStack.push(-3)
    print(maxStack.peekMax())
