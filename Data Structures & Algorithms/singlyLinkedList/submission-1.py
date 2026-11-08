class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, i):
        if i >= self.size or i < 0:
            return -1
        cur = self.head
        j = 0
        while (j < i):
            cur = cur.next
        return cur.val
    
    def insertHead(self, val):
        node = ListNode(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size+=1
    
    def insertTail(self, val):
        node = ListNode(val)
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size+=1
    
    def remove(self, i):
        if i < 0 or i >= self.size:
            return False
        if i == 0:
            self.head = self.head.next
        
        j = 0
        cur = self.head
        while j < i-1:
            cur = cur.next
        
        if i == self.size - 1:
            self.tail = cur
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            cur.next = cur.next.next
        self.size-=1
        return True
    
    def getValues(self):
        arr = []
        cur = self.head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr

        
    


        



        
