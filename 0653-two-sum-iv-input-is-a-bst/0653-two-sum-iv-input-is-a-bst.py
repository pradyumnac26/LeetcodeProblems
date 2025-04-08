# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        x = [] 

        def inorder(root, x): 

            if root is None : 
                return
            
            inorder(root.left, x)
            x.append(root.val)
            inorder(root.right, x)
        
        inorder(root, x)
        
        l = 0
        r = len(x) - 1 
        while l < r : 
            if x[l] + x[r] > k : 
                r = r - 1 
            elif x[l] + x[r] <  k : 
                l = l +1 
            else : 
                return True
        return False
