class Node:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        i = 0
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        while i < index:
            cur = cur.next
            i+=1
        return cur.val

        

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        if not self.head:
            self.head = new
        else:
            new.next = self.head
            self.head = new
        self.size+=1
    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(val)
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
            return
        if index > self.size:
            return
        cur = self.head
        i = 0
        while i < index - 1:
            cur = cur.next
            i+=1
        nxt = cur.next
        cur.next = Node(val, nxt)
        self.size+=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            return
        prev = None
        cur = self.head
        i = 0
        while i < index:
            prev = cur
            cur = cur.next
            i+=1
        prev.next = cur.next
        self.size-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)