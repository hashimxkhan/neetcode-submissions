class ListNode:

    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = ListNode(homepage)
        self.cur = self.home
        
    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.cur
        self.cur.next = node
        self.cur = self.cur.next
        

    def back(self, steps: int) -> str:
        cur = self.cur
        while cur.prev:
            cur = cur.prev
            steps-=1
            if steps == 0:
                self.cur = cur
                return cur.val
        self.cur = cur
        return cur.val
        

    def forward(self, steps: int) -> str:
        cur = self.cur
        while cur.next:
            cur = cur.next
            steps-=1
            if steps == 0:
                self.cur = cur
                return cur.val
        self.cur = cur
        return cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)