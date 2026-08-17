class Node:

    def __init__(self, val, counter, key=None, next=None, prev=None):
        self.val = val
        self.counter = counter
        self.next = next
        self.prev = prev
        self.key = key

class LFUCache:

    def __init__(self, capacity: int):
        self.keys = {}
        self.capacity = capacity
        self.head = Node(0,float('inf'))
        self.tail = Node(0,float('inf'))
        self.head.next = self.tail
        self.head.prev = self.tail
        self.tail.next = self.head
        self.tail.prev = self.head
        self.count = 0

    def get(self, key: int) -> int:
        if key in self.keys:
            self.keys[key].counter+=1
            node = self.keys[key]
            prev = node.prev
            prev.next = node.next
            node.next.prev = prev
            prev = self.tail.prev
            prev.next = node
            node.prev = prev
            self.tail.prev = node
            node.next = self.tail
            return self.keys[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.keys[key].val = value
            self.keys[key].counter+=1
            return
        
        if self.count == self.capacity:
            mini = float('inf')
            cur = self.head.next
            while cur != self.head:
                mini = min(mini, cur.counter)
                cur = cur.next
            
            cur = self.head.next
            while cur != self.head:
                if cur.counter == mini:
                    prev = cur.prev
                    prev.next = cur.next
                    cur.next.prev = prev
                    self.count-=1
                    self.keys.pop(cur.key, None)
                    break
                cur = cur.next

        new = Node(value, 1, key)
        self.keys[key] = new
        prev = self.tail.prev
        prev.next = new
        new.prev = prev
        self.tail.prev = new
        new.next = self.tail
        self.count+=1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)