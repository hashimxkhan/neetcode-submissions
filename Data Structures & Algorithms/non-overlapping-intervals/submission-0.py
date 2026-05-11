class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        total = 0
        curInterval = intervals[0]
        for i in range(1,len(intervals)):
            if curInterval[1] > intervals[i][0]:
                total+=1
                curInterval = [curInterval[0], min(curInterval[1], intervals[i][1])]
            else:
                curInterval = intervals[i]
        return total