class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        times = []
        for i in range(len(tasks)):
            times.append((tasks[i][0], tasks[i][1], i))
        
        heapq.heapify(times)
        curTime = times[0][0]
        ret = []
        available = []
        while times:
            cur = []
            if curTime < times[0][0]:
                curTime = times[0][0]
            while times and times[0][0] <= curTime:
                newTask = heapq.heappop(times)
                push = (newTask[1], newTask[2])
                heapq.heappush(available, push)            

            task = heapq.heappop(available)
            ret.append(task[1])
            curTime+=task[0]

        while available:
            cur = heapq.heappop(available)
            ret.append(cur[1])
        
        return ret
