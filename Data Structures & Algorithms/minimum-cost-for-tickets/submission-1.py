class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}

        def dp(i, covered):
            if i >= len(days):
                return 0

            if (i, covered) in memo:
                return memo[(i,covered)]

            if covered > days[i]:
                return dp(i+1, covered)
            
            memo[(i,covered)] = min(costs[0] + dp(i+1, days[i] + 1), costs[1] + dp(i+1, days[i] + 7), costs[2] + dp(i+1, days[i] + 30))
            return memo[(i,covered)]
        return dp(0,0)
        