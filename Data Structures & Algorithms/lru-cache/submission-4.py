class Node:

    def __init__(self, key: int, val: int, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        prev = node.prev
        after = node.next
        prev.next = after
        after.prev = prev

    def insert(self, node):
        after = self.head.next
        node.next = after
        after.prev = node
        node.prev = self.head
        self.head.next = node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]



        
