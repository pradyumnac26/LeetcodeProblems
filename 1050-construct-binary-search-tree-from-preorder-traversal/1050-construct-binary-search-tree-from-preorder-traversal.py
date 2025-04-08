# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.index = 0  # Global index to track root position in preorder

        def helper(lower=float('-inf'), upper=float('inf')):
            if self.index == len(preorder):
                return None

            val = preorder[self.index]
            if not (lower < val < upper):
                return None

            self.index += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root

        return helper()
