# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, path) : 
            if not root : 
                return path 
            if root.left is None and root.right is None : 
                path.append(root.val) 
                return path
            dfs(root.left, path)
            dfs(root.right, path)
            return path

        leaves1 = [] 
        leaves2 = []
        leaves1 = dfs(root1, leaves1) 
        leaves2 = dfs(root2, leaves2) 
        return leaves1 == leaves2
            
        