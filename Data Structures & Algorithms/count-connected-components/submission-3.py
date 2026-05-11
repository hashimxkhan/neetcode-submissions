class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        visited = set()
        res = 0
        if not edges:
            return n
        for i in range(n):
            adj[i] = []
        for edge in edges:
            a,b = edge
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)
            


        for node in adj:
            if node not in visited:
                res+=1
                dfs(node)
        return res

