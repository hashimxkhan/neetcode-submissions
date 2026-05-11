"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hashMap = {}
        def dfs(node):
            if node in hashMap:
                return hashMap[node]
            cpy = Node(node.val)
            hashMap[node] = cpy
            for n in node.neighbors:
                cpy.neighbors.append(dfs(n))
            return cpy
        dfs(node)
        return hashMap[node]



        # have a hashmap and create a copy for each node and map original to hashmap during dfs
        # go thru each node in hashmap and connect nodes neighbours copies to copies
        # return "head"
            