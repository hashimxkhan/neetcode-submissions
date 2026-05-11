class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        total = 0

        adj = defaultdict(list)
        for edge in edges:
            u, v = edge[0], edge[1]
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            if node not in visited:
                visited.add(node)
                for nei in adj[node]:
                    dfs(nei)
        
        for v in adj:
            if v not in visited:
                dfs(v)
                total+=1
        total = total + (n - len(visited))
        return total

