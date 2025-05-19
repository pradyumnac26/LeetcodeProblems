# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0 
        def dfs(root, sumi) : 
            if root is None: 
                return 
            sumi = sumi + str(root.val)
            if not root.left and not root.right :
                self.res = self.res + int(sumi, 2)
            dfs(root.left, sumi)
            dfs(root.right, sumi)




        dfs(root, "")
        return self.res


        
        