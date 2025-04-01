from collections import defaultdict, deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return [] 
        
        queue = deque([(root, 0 , 0)])  # node, column, level
        col_table = defaultdict(list)

        while queue: 
            node, col, level = queue.popleft()
            col_table[col].append((level, node.val))
            
            if node.left: 
                queue.append((node.left, col - 1, level + 1))
            if node.right: 
                queue.append((node.right, col + 1, level + 1))

        result = []
        for col in sorted(col_table.keys()): 
            # Sort first by level, then by value
            col_table[col].sort()
            x = [val for level, val in col_table[col]]
            result.append(x)
        
        return result
