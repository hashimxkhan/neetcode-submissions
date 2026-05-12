class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append(price)
            return 1
        
        i = len(self.stack) - 1
        while i >= 0:
            if price < self.stack[i]:
                self.stack.append(price)
                return len(self.stack) - i - 1
            i-=1
        self.stack.append(price)
        return len(self.stack)
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)