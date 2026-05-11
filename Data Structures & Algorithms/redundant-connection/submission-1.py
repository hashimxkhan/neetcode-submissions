class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # cycle detection dfs
        parent, size = [], []
        for i in range(len(edges)):
            parent.append(i)
            size.append(1)
        
        def find(x):
            cur = x
            while parent[cur] != cur:
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]
            return cur
        
        def union(x, y):
            node1, node2 = find(x), find(y)
            if node1 == node2:
                return False

            if size[node2] > size[node1]:
                parent[node1] = node2
                size[node2]+= size[node1]
            else:
                parent[node2] = node1
                size[node1]+= size[node2]
            return True
        
        for edge in edges:
            x,y = edge
            if not union(x-1,y-1):
                return [x,y]

            



