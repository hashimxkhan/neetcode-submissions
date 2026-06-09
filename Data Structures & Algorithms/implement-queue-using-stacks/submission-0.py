class MyQueue:

    def __init__(self):
        self.front = []
        self.back = []

    def push(self, x: int) -> None:
        self.back.append(x)

    def pop(self) -> int:
        if self.front:
            return self.front.pop(0)
        else:
            if not self.back:
                return
            else:
                self.front = self.back
                self.back = []
                return self.front.pop(0)

    def peek(self) -> int:
        if self.front:
            return self.front[0]
        else:
            return self.back[0]

        

    def empty(self) -> bool:
        if not self.front and not self.back:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()