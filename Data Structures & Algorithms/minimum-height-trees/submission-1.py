class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for edge in edges:
            a,b = edge
            adj[a].append(b)
            adj[b].append(a)
        

        def dfs(node, parent):
            height = 0
            for n in adj[node]:
                if n != parent:
                    height = max(height, 1 + dfs(n, node))
            return height
        
        minH = float('inf')

        ret = []
        for i in range(n):
            height = dfs(i, -1)
            if height == minH:
                ret.append(i)
            elif height < minH:
                ret = []
                ret.append(i)
                minH = height
        return ret
