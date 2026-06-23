class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        memo = {}
        def dp(r, c1):
            if r >= len(points):
                return 0

            if (r,c1) in memo:
                return memo[(r,c1)]

            best = float('-inf')
            if c1 == -1:
                for i in range(len(points[0])):
                    best = max(best, points[r][i] + dp(r+1, i))
            else:
                for i in range(len(points[0])):
                    best = max(best, points[r][i] - abs(c1 - i) + dp(r+1, i))
            
            memo[r,c1] = best
            return best
        
        return dp(0,-1)
        
