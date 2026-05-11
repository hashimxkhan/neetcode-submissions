"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        res = 0
        count = 0
        s = 0
        e = 0

        while s < len(start):
            if start[s] < end[e]:
                count+=1
                s+=1
            else:
                e+=1
                count-=1
            res = max(count, res)
        return res


