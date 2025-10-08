# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = [] 
        st = [] 
        def dfs(root, st) : 
            if not root : 
                return 
            if not root.left and not root.right : 
                res.append(''.join([chr(ord('a') + root.val)] + st))
                return 



            dfs(root.left, [chr(ord('a') + root.val)] + st)
            dfs(root.right, [chr(ord('a') + root.val)]  + st )



        dfs(root, st)
        res.sort()
        print(res)
        return res[0]
        