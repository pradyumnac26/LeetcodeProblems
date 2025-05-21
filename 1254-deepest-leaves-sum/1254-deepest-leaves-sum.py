# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:



        def height(root) : 
            if not root : 
                return 0 
            left = height(root.left)
            right = height(root.right)
            return 1 + max(left, right)
        max_depth = height(root)

        x = 0 
        def dfs(root, depth): 
            nonlocal x
            if root is None : 
                return  
            if depth == max_depth : 
                x = x + root.val
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 1)
        return x


