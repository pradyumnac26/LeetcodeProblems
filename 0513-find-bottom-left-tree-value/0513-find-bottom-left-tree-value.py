# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # leftmost value in the last row of the tree. 
        q = deque([root]) 
        res = [] 
        while q : 
            level = [] 
            for _ in range(len(q)): 
                root = q.popleft() 
                level.append(root.val)
                if root.left : 
                    q.append(root.left)
                if root.right : 
                    q.append(root.right)
            res.append(level)
        return res[-1][0]
                    




        