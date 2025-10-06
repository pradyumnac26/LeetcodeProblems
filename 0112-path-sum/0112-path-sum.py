# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, sumi) : 
            if not root : 
                return False
            if not root.left and not root.right  : 
                return targetSum == sumi+root.val

            ans1 = dfs(root.left, sumi+root.val)
            ans2 = dfs(root.right, sumi+root.val) 
            return  ans1 or ans2 

        if root is None : 
            return False
        return dfs(root, 0)

        