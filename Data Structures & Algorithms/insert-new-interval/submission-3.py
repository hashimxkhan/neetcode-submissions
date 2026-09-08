class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        flag = False
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                ret.append(newInterval)
                flag = True
                ret = ret + intervals[i:]
                return ret
            elif newInterval[0] <= intervals[i][1]:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            
            else:
                ret.append(intervals[i])
        if not flag:
            ret.append(newInterval)
        return ret
            



        