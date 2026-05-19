class Node:

    def __init__(self):
        self.val = None
        self.prev = None
        self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.head = Node()
        cur = self.head
        for i in range(k-1):
            cur.next = Node()
            cur = cur.next
        cur.next = self.head
        self.tail = self.head
        self.count = 0
        self.k = k
        self.rear = None
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.tail.val = value
        self.rear = self.tail
        self.tail = self.tail.next
        self.count+=1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head.val = None
        self.head = self.head.next
        self.count-=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.val
        

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()