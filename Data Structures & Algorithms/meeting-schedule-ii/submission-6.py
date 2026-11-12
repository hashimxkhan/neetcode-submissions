"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        intervals.sort(key=lambda x : (x.start, x.end))
        size = 0
        for interval in intervals:
            if not heap or heap[0] > interval.start:
                heapq.heappush(heap, interval.end)
            size = max(size, len(heap))
        return size
