class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        intervals = []

        for i in range(len(startTime)):
            tup = [startTime[i], endTime[i], profit[i]]
            intervals.append(tup)
        
        intervals.sort(key=lambda x: (x[0], x[1], x[2]))
        memo = {}
        def dp(i, free):
            if i >= len(intervals):
                return 0
            if (i,free) in memo:
                return memo[(i,free)]
            if intervals[i][0] >= free:
                take = intervals[i][2] + dp(i+1, intervals[i][1])
                leave = dp(i+1, free)
                memo[(i,free)] = max(take,leave)
                return memo[(i,free)]
            else:
                memo[(i,free)] = dp(i+1, free)
                return memo[(i,free)]
        
        return dp(0,0)

        