class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        adj = set()
        if not edges and n <= 1:
            return 0
        if not edges:
            return -1
        for edge in edges:
            u, v = edge
            adj.add(v)

        ct = 0
        res = -1
        print(adj)
        print(edges)
        for edge in edges:
            u,v = edge
            if u not in adj and u != res:
                res = u
                ct+=1
        if ct != 1:
            return -1
        return res

