class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            minValue = val
        else:
            minValue = min(val, self.minStack[-1])
        self.stack.append(val)
        self.minStack.append(minValue)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
