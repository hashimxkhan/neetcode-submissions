class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = []
        size = []
        for i in range(n):
            parent.append(i)
            size.append(1)
        
        def find(x):
            cur = x
            while cur != parent[cur]:
                parent[cur] = parent[parent[cur]] # make curs parent = parents parents
                cur = parent[cur]
            return cur
        
        def union(x, y):
            n1, n2 = find(x), find(y)

            if n1 == n2: # same group
                return 0
            
            if size[n1] > size[n2]:
                parent[n2] = n1
                size[n1]+= size[n2]
            else:
                parent[n1] = n2
                size[n2]+= size[n1]
            return 1
        
        res = n
        for edge in edges:
            a,b = edge
            res-= union(a,b)
        return res



        



