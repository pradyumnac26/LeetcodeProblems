from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Step 1: Calculate the sum of nodes at each level
        level_sums = []
        queue = deque([root])
        
        while queue:
            cur_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                cur_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_sums.append(cur_sum)

        # Step 2: Modify the node values based on sibling sums
        queue = deque([(root, root.val)])  # (node, child_sum)
        level = 0
        
        while queue:
            for _ in range(len(queue)):
                node, val = queue.popleft()
                node.val = level_sums[level] - val  # Subtract the child sum from the level sum
                
                child_sum = 0
                if node.left:
                    child_sum += node.left.val
                if node.right:
                    child_sum += node.right.val
                
                if node.left:
                    queue.append((node.left, child_sum))
                if node.right:
                    queue.append((node.right, child_sum))
            level += 1

        # Step 3: Set root node's value to 0
        root.val = 0

        return root
