class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            arr.append([position[i], speed[i]])
        arr.sort(key=lambda x: x[0])
        maxTime = 0
        fleets = 0
        for i in range(len(arr)-1, -1, -1):
            curTime = (target - arr[i][0]) / arr[i][1]
            if curTime > maxTime:
                fleets+=1
                maxTime = curTime
        return fleets
            
