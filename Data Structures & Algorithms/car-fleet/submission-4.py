class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stats = []
        for i in range(len(position)):
            stats.append((position[i], speed[i]))
        stats.sort(reverse = True)
        
        slowest = 0
        res = 0
        for pos, sp in stats:
            time = (target - pos) / sp
            if time > slowest:
                res+=1
                slowest = time
        return res


        