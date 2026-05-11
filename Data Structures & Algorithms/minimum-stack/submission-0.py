class Node:
    def __init__(self, min_val, val):
        self.min_val = min_val
        self.val = val
        self.next = None

class MinStack:

    def __init__(self):
        self.head = None
        
    def push(self, val: int) -> None:
        if self.head == None:
            minValue = val
        else:
            minValue = min(val, self.head.min_val)
        cur = Node(minValue, val)
        cur.next = self.head
        self.head = cur
        

    def pop(self) -> None:
        self.head = self.head.next
        

    def top(self) -> int:
        return self.head.val
        

    def getMin(self) -> int:
        return self.head.min_val
        
