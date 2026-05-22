class Node:

    def __init__(self, val=None, key=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.mapping = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
    
    def insert(self, node):
        nxt = self.head.next
        self.head.next = node
        node.next = nxt
        node.prev = self.head
        nxt.prev = node
    
    def remove(self, node):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev


    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        node = self.mapping[key]
        self.remove(node)
        self.insert(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.remove(self.mapping[key])
            self.size-=1

        node = Node(value, key)
        self.mapping[key] = node
        self.insert(node)
        self.size+=1
        if self.size > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del(self.mapping[lru.key])
            self.size-=1

        
