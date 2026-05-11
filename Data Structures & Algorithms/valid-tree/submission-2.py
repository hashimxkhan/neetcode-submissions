class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1- needs to have n-1 edges
        # 2- needs to connected 
        # 3- no cycles (track parent here)

        # dfs cycle but use parent
        if len(edges) != n-1: # needs to be connected
            return False
        adj = {}
        for i in range(n):
            adj[i] = []
        
        # build adj list
        for edge in edges:
            parent, child = edge
            adj[parent].append(child)
            adj[child].append(parent)
        
        # j detect cycles here with the parent caveat
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        

        return dfs(0,-1) and len(visited) == n

