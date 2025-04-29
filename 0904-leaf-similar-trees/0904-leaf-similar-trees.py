# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        x1 = [] 
        x2 = [] 
        def dfs(root, result): 
            if root is None : 
                return 
            if root.left is None and root.right is None: 
                result.append(root.val)
                return
            
            dfs(root.left, result)
            dfs(root.right, result)
        
        dfs(root1,x1)
        dfs(root2,x2)
        return x1==x2
        
        
        