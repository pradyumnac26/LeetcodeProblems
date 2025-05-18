# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0 
        def dfs(node) : 

            if node is None : 
                return 0 
            
            lh = dfs(node.left)
            rh = dfs(node.right)
            lpath = rpath = 0 
            if node.left and node.val == node.left.val : 
                lpath = lh + 1 
            if node.right and node.val == node.right.val : 
                rpath = rh + 1 
            self.maxi = max(self.maxi, lpath + rpath )
            return max(lpath, rpath )

        dfs(root)
        return self.maxi 


        