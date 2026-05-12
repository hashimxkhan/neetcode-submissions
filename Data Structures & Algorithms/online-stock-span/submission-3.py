class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price, 1))
            return 1
        
        i = len(self.stack) - 1
        span = 1
        while self.stack and i >= 0:
            if price >= self.stack[i][0]:
                cur = self.stack.pop()
                span+= cur[1]
                i-=1
            else:
                break
        self.stack.append((price, span))
        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)