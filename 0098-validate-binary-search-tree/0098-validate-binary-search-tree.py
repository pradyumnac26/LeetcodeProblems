# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))
    
    def validate(self, node: Optional[TreeNode], low: float, high: float) -> bool:
        # An empty tree is a valid BST
        if node is None:
            return True
        # Check if the current node's value is within the valid range
        if not (low < node.val < high):
            return False
        # Recursively check the left and right subtrees
        return (self.validate(node.left, low, node.val) and 
                self.validate(node.right, node.val, high))
        