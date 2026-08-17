class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        times = []
        for i in range(len(tasks)):
            times.append((tasks[i][0], tasks[i][1], i))
        
        heapq.heapify(times)
        curTime = times[0][0]
        ret = []
        while times:
            cur = []
            if curTime < times[0][0]:
                curTime = times[0][0]
            while times and times[0][0] <= curTime:
                cur.append(heapq.heappop(times))
            
            cur.sort(key=lambda x: (x[1], x[2]))

            task = cur[0]
            ret.append(cur[0][2])
            curTime+=cur[0][1]
            for i in range(1, len(cur)):
                heapq.heappush(times, cur[i])
        
        return ret
