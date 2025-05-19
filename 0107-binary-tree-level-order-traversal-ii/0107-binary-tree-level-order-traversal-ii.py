# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        q= deque([root])
        res = [] 
        if not root : 
            return []
        
        while q : 
            level = [] 
            for i in range(len(q)) : 
                node = q.popleft()
                level.append(node.val)
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
            res.append(level)
        print(res)
        rev = []
        for i in range(len(res)-1, -1, -1) : 
            rev.append(res[i])
        return rev


        