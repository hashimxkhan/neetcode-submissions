class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # key to ListNode
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node
    
    def remove(self, node):
        nxt = node.next
        prev = node.prev
        prev.next = nxt
        nxt.prev = prev

    
    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = ListNode(key, value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]

    


        
