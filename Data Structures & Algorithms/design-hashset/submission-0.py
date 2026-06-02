class MyHashSet:

    def __init__(self):
        self.arr = []

    def add(self, key: int) -> None:
        self.arr.append(key)

    def remove(self, key: int) -> None:
        i = 0
        while i < len(self.arr):
            if self.arr[i] == key:
                self.arr.pop(i)
                i-=1
            i+=1

    def contains(self, key: int) -> bool:
        for i in range(len(self.arr)):
            if self.arr[i] == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)