# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([(root, None)])
        while q : 
            x_parent = -1 
            y_parent = -1 
            for _ in range(len(q)) : 
                node, parent = q.popleft() 
                if node.val == x : 
                    x_parent = parent 
                if node.val == y : 
                    y_parent = parent

                if node.left : 
                    q.append((node.left, node))
                if node.right : 
                    q.append((node.right, node))
                
            if x_parent != -1  and y_parent!=-1 and x_parent != y_parent : 
                return True 
        return False