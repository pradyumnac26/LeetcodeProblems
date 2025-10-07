# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])
        if root is None : 
            return []
        while q : 
            level = [] 
            for _ in range(len(q)) : 
                node = q.popleft()
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
                level.append(node.val)
            res.append(level)
        return res 
        