# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(root, path, target):
            if not root : 
                return False
            if root.val == target : 
                return path


            path.append("L")
            res = dfs(root.left, path, target)
            if res : 
                return res
            path.pop()
            path.append("R")
            res = dfs(root.right, path, target) 
            if res : 
                return res
            path.pop()
            return False


        start = [] 
        end = [] 
        start_path = dfs(root, start, startValue)
        end_path = dfs(root, end, destValue)
        i = 0 
        while i < min(len(start_path), len(end_path)): 
            if start_path[i] != end_path[i]: 
                break
            i = i + 1

        st = ["U"]*len(start_path[i:]) + end_path[i:]
        return "".join(st)


        