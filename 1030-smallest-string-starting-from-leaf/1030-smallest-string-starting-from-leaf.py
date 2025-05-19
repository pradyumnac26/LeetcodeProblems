# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.z = "~"
        def dfs(root, s): 
            if not root : 
                return 

            s = chr(root.val+97) + s  
            if not root.left and not root.right : 
                self.z = min(self.z, s)
            

            dfs(root.left, s)
            dfs(root.right, s)





        dfs(root, "")
        return self.z
        