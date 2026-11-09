class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.index = {}
        self.size = 0


    def get(self, i: int) -> int:
        return self.index[i]

    def set(self, i: int, n: int) -> None:
        self.index[i] = n

    def pushback(self, n: int) -> None:
        self.index[self.size] = n
        self.size+=1
        if self.size > self.capacity:
            self.resize()


    def popback(self) -> int:
        if self.size == 1:
            self.head.next = None
            val = self.index[0]
            del self.index[0]
            return val
        val = self.index[self.size-1]
        del self.index[self.size - 1]
        self.size-=1
        return val

    def resize(self) -> None:
        self.capacity = self.capacity * 2


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity