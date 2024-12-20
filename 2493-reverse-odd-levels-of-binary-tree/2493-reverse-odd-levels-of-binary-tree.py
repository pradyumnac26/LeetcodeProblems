# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self,root):
        if not root:
            return None

        def dfs(node1, node2, level):
            if not node1 or not node2:
                return

        # Reverse values at odd levels
            if level % 2 == 1:
                node1.val, node2.val = node2.val, node1.val

        # Continue for the next level
            dfs(node1.left, node2.right, level + 1)
            dfs(node1.right, node2.left, level + 1)

        dfs(root.left, root.right, 1)  # Start with level 0
        return root

        