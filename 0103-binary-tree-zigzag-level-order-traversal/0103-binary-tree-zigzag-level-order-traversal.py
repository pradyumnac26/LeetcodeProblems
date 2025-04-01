# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : 
            return []
        queue = deque([root])
        result = [] 
        flag = 1
        while queue : 

            level = deque()
            for i in range(len(queue)) : 
                node = queue.popleft()
                if flag : 
                    level.append(node.val)
                else : 
                    level.appendleft(node.val)
                
                if node.left : 
                    queue.append(node.left)
                if node.right : 
                    queue.append(node.right)
            result.append(list(level))
            flag = not flag
        return result
                
        