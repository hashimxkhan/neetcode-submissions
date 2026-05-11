class LRUCache:

    def __init__(self, capacity: int):
        self.arr = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        for i in range(len(self.arr)):
            if self.arr[i][0] == key:
                value = self.arr[i][1]
                del self.arr[i]
                self.arr.insert(0,[key,value])
                return value
        print(self.arr)
        return -1
        

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.arr)):
            if self.arr[i][0] == key:
                del self.arr[i]
                new = [key, value]
                self.arr.insert(0,new)
                return
        self.arr.insert(0, [key,value])
        if len(self.arr) > self.capacity:
            del self.arr[len(self.arr)-1]