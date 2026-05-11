class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # dfs cycle but use parent
        if len(edges) < n-1: # needs to be connected
            return False
        adj = {}
        for i in range(n):
            adj[i] = []
        for edge in edges:
            parent, child = edge
            adj[parent].append(child)
            adj[child].append(parent)
        
        visiting = set()
        def dfs(n, parent):
            if n in visiting:
                return False
            visiting.add(n)
            for neighbor in adj[n]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, n):
                    return False
            return True

        return dfs(0,-1)

