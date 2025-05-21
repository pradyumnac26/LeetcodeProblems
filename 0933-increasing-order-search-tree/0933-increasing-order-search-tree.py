# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def inorder(root, res) : 
            if root is None : 
                return 
            inorder(root.left, res)
            res.append(root.val) 
            inorder(root.right, res)
        res= [] 
        inorder(root, res)
        x = TreeNode(val = res[0])
        tmp = x
        for i in res[1:] : 
            tmp.right = TreeNode(val=i)
            tmp = tmp.right
        return x

        