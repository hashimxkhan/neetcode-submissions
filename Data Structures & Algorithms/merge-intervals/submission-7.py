class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : (x[0], x[1]))
        merged = []
        cur = intervals[0]
        for i in range(1, len(intervals)):
            if cur[1] >= intervals[i][0]:
                cur = [cur[0], max(cur[1], intervals[i][1])]
            else:
                merged.append(cur)
                cur = intervals[i]
        merged.append(cur)
        return merged

