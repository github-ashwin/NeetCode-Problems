from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        # LAST IN FIRST OUT
        # Popping it from the left - adding it to the right
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft() # Returns the last value

    def top(self) -> int:
        return self.queue[len(self.queue)-1] # Right-most value

    def empty(self) -> bool:
        return len(self.queue)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()