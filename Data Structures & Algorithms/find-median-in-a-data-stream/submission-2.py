class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []  
        self.leftSize = 0
        self.rightSize = 0

    def addNum(self, num: int) -> None:
        if self.leftSize == 0 and self.rightSize == 0:
            self.leftSize+=1
            heapq.heappush(self.left, -num)
            return
        if self.leftSize == self.rightSize:
            if self.right[0] >= num:
                heapq.heappush(self.left, -num)
                self.leftSize+=1
            else:
                heapq.heappush(self.right, num)
                self.rightSize+=1
        elif self.leftSize < self.rightSize:
            if self.right[0] < num:
                val = heapq.heappop(self.right)
                heapq.heappush(self.right, num)
                heapq.heappush(self.left, -val)
                self.leftSize+=1
            else:
                heapq.heappush(self.left, -num)
                self.leftSize+=1
        
        else:
            if (self.left[0] * - 1) > num:
                val = heapq.heappop(self.left)
                heapq.heappush(self.left, -num)
                heapq.heappush(self.right, -val)
                self.rightSize+=1
            else:
                heapq.heappush(self.right, num)
                self.rightSize+=1

                
    def findMedian(self) -> float:
        if self.rightSize == self.leftSize:
            return (self.right[0] + (self.left[0] * -1)) / 2
        elif self.rightSize > self.leftSize:
            return self.right[0]
        else:
            return self.left[0] * -1
        
        