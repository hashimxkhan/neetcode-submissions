class FreqStack:

    def __init__(self):
        self.stack = {}
        self.last = {}
        self.cur = 0
    def push(self, val: int) -> None:
        if val not in self.stack:
            self.stack[val] = 0
            self.last[val] = []
        self.stack[val]+=1
        self.last[val].append(self.cur)
        self.cur+=1
    def pop(self) -> int:
        maxi = 0
        for key in self.stack:
            maxi = max(self.stack[key], maxi)
        
        last = 0
        ret = 0
        for key in self.stack:
            if self.stack[key] == maxi and self.last[key][-1] >= last:
                ret = key
                last = self.last[key][-1]
        self.stack[ret]-=1
        self.last[ret].pop()
        return ret


        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()