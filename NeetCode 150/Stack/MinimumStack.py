class MinStack:

    def __init__(self):
        self.stack = [] # stores correct values
        self.minstack = [] # stores current minimum values

    def push(self, val: int) -> None:
        # append to both
        self.stack.append(val)
        minval = min(val,self.minstack[-1] if self.minstack else val)
        self.minstack.append(minval)

    def pop(self) -> None:
        # pop from both
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1] # return top value in stack

    def getMin(self) -> int:
        return self.minstack[-1] # return top value in minstack
