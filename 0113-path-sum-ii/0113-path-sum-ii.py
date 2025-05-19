# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, path, sumi): 
            if node is None : 
                return 
            path.append(node.val)
            sumi = sumi + node.val
            if not node.left and not node.right and sumi == targetSum : 
                res.append(path[:])
            dfs(node.left, path, sumi)
            dfs(node.right, path, sumi)
            path.pop()
        res = []
        dfs(root, [], 0)
        return res
            








        dfs(root, [], 0)

        