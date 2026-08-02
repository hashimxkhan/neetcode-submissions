# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.data = ""
        def dfs(root):
            if not root:
                self.data+="N,"
                return
            val = str(root.val)
            self.data = self.data + val + ","
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.data

            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = []
        cur = ""
        for c in data:
            if c != ',':
                cur+=c
            else:
                arr.append(cur)
                cur = ""
        print(arr)
        if not arr:
            return []
        self.head = None
        self.i = 0
        def dfs():
            if arr[self.i] == 'N':
                self.i+=1
                return None
            node = TreeNode(int(arr[self.i]))
            if self.i == 0:
                self.head = node
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        
        dfs()
        return self.head

            
            

