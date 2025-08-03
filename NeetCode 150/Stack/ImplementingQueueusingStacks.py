from collections import deque
class MyQueue:

    def __init__(self):
        # self.stack = deque()
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # self.stack.append(x)
        self.s1.append(x)

    def pop(self) -> int:
        # return self.stack.popleft()
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        # return self.stack[0]
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        # return len(self.stack)==0
        return max(len(self.s1),len(self.s2)) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()