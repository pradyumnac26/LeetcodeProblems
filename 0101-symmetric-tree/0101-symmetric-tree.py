# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        # If both nodes are None, they are mirrors
        if node1 is None and node2 is None:
            return True
        # If only one of the nodes is None, they are not mirrors
        if node1 is None or node2 is None:
            return False
        # Check if the current nodes' values are equal and the subtrees are mirrors
        return (node1.val == node2.val and 
                self.isMirror(node1.left, node2.right) and 
                self.isMirror(node1.right, node2.left))