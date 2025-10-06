# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        x = "" 
        res = [] 
        def dfs(root, x, res): 
            if not root : 
                return 
            x = x + str(root.val)
            if not root.left and not root.right: 

                res.append(x)
                return 
            
            dfs(root.left, x, res)
            dfs(root.right, x , res)
            
                

        dfs(root, x, res)
        sumi = 0 
        for i in res : 
            sumi = sumi + int(i)
        return sumi



        