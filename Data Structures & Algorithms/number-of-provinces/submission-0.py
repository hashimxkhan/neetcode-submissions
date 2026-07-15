class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j] == 1:
                    adj[i].append(j)
        visited = set()
        def dfs(node):
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        count = 0

        for i in range(n):
            if i not in visited:
                count+=1
                visited.add(i)
                dfs(i)
        return count