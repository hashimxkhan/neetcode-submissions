class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        curInterval = intervals[0]
        ret = []
        for i in range(len(intervals)):
            if curInterval[1] >= intervals[i][0]:
                curInterval = [min(curInterval[0], intervals[i][0]), max(curInterval[1], intervals[i][1])]
            else:
                ret.append(curInterval)
                curInterval = intervals[i]
        ret.append(curInterval)
        return ret