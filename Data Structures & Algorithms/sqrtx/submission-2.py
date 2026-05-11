class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        for i in range(x):
            if i*i == x:
                return i
            
            if i*i > x:
                return i-1
        