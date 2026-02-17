# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # soneed to check  all root to leaf path sum , and check if it has targetSum, if yes then done. return true 
        if root is None : 
            return False

        def dfs(root, res) : 
            if root is None : 
                return 
            if root.left is None and root.right is None : 
                res.append(root.val)
                final.append(sum(res))
                return


            dfs(root.left, res + [root.val]) 
            dfs(root.right, res + [root.val])
        
        final = [] 
        res = [] 
        dfs(root, res)

        for i in final : 
            if i == targetSum : 
                return True 
        return False 
        