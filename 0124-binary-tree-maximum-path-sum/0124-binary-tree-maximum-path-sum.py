# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def maxpath(root) : 
            nonlocal maxi
            if root is None : 
                return 0 
            lh = max(0, maxpath(root.left))
            rh = max(0, maxpath(root.right))
            
            maxi = max(maxi, lh + rh + root.val)
            return root.val + max(lh, rh)
        maxi = float("-inf")
        maxpath(root)
        return maxi
        