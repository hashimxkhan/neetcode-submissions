class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to the node
        self.right, self.left = Node(0,0), Node(0,0)
        self.right.prev = self.left
        self.left.next = self.right

    def remove(self, node):
        # we remove from left
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # also update when u put so delete and insert
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            # remove node from left
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
