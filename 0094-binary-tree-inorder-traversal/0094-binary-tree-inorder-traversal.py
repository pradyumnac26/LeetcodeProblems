# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node, b):
            if node is not None:
                helper(node.left, b)
                b.append(node.val)
                helper(node.right, b)
        
        result = []
        helper(root, result)
        return result