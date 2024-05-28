# The idea here is to have two stacks in the class.
# We push to the stack and pop from to both of them:
# 1. The general stack
# 2. The stack that has the min values.
# For each push operation, we will do a min operation between the last min and the current val and add the updated min the the min_values stack
# For each pop operation, we will pop from the top of the min_values stack as well.
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_values = []

    def push(self, val: int) -> None:
        if not self.is_empty():
            self.min_values.append(min(val, self.min_values[-1]))  # add the new min to the min_values stack
        else:
            self.min_values.append(val)  # if the stack is empty, the first entry will me the min
        self.stack.append(val)  # add to the stack

    def pop(self) -> None:
        if not self.is_empty():  # pop from both of the stacks if the stack is not empty
            self.stack.pop()
            self.min_values.pop()

    def top(self) -> int:
        if not self.is_empty():  # retrieve the value (peeking) - without poping it out
            return self.stack[-1]
        return -1

    def getMin(self) -> int:
        if not self.is_empty():
            return self.min_values[-1]  # get the min value from the top of the min_values
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
