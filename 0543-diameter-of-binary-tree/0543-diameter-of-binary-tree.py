# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # length of longest path between any 2 nodes in a tree. , and may or may not pass through the root. 
        #number of edges between them 
        def dfs(root) : 
            nonlocal diam
            if not root : 
                return 0 

            lh = dfs(root.left)
            rh = dfs(root.right) 
            diam = max(diam, lh + rh)
            return 1 + max(lh, rh) 
        diam = 0
        dfs(root)
        return diam       