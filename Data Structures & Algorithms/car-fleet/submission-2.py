class Solution:
    import math
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sAndP = []
        for i in range(len(position)):
            sAndP.append([position[i], speed[i]])
        
        sAndP.sort(key=lambda x:x[0], reverse = True)
        total = 0
        slowest = 0
        for p,s in sAndP:
            time = (target - p) / s
            if time > slowest:
                slowest = time
                total+=1
        return total


