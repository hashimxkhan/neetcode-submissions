"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x : (x.start, x.end))
        cur = intervals[0]
        for i in range(1, len(intervals)):
            if cur.end > intervals[i].start:
                return False
            cur = intervals[i]
        return True
