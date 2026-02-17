# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(root, path) : 
            if root is None : 
                return 
            if root.left is None and root.right is None : 
                path.append(root.val) 
                if sum(path) == targetSum : 
                    final.append(path)
                return

            dfs(root.left, path + [root.val] ) 
            dfs(root.right, path + [root.val])

        final = [] 
        dfs(root, [])
        return final



        