class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        rows = len(points)
        cols = len(points[0])
        cache = {}
        def dp(r, prevCol):
            if r == rows:
                return 0
            if (r, prevCol) in cache:
                return cache[(r,prevCol)]
            best = float('-inf')
            for c in range(cols):
                if r == 0:
                    best = max(best, points[r][c] + dp(r+1, c))
                else:
                    best = max(best, points[r][c] + dp(r+1, c) - abs(prevCol - c))
            cache[(r, prevCol)] = best
            return best
        
        return dp(0, -1)

                
