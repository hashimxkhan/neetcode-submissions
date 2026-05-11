class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next, self.prev = None,   None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node):
        nxt = self.head.next
        self.head.next = node
        node.next = nxt
        node.prev = self.head
        nxt.prev = node
    
    def remove(self, node):
        prv = node.prev
        prv.next = node.next
        node.next.prev = prv


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]


        
