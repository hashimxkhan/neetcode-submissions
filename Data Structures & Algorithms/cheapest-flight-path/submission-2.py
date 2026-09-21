class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = {}
        for f in flights:
            if f[0] not in adj:
                adj[f[0]] = []
            adj[f[0]].append([f[1], f[2]])

        cache = {}
        def cheapest(cur, stops):
            if (cur, stops) in cache:
                return cache[(cur,stops)]
            if stops > k + 1:
                return float('inf')
            
            if cur == dst:
                return 0
            
            best = float('inf')
            if cur in adj:
                for f in adj[cur]:
                    new = f[1] + cheapest(f[0], stops+1)
                    best = min(new, best)
            cache[(cur, stops)] = best
            return best
        
        price = cheapest(src, 0)
        if price == float('inf'):
            return -1
        return price
            

            

        