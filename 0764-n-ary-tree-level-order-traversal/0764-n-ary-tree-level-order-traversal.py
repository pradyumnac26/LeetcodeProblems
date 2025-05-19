"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if root is None :
            return None
        q = deque([root])
        while q : 
            size = len(q)
            level = [] 
            for i in range(len(q)) : 
                node = q.popleft()
                level.append(node.val)
                if node.children: 
                    q.extend(node.children)
            res.append(level)
        return res
        