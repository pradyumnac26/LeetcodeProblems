# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # return the level with maximum sum 
        # so what i can do is , i can just do the level order traversal , and then on each level just caclulate the sum whcih is minimal and thn return the level with least sum, 
        # one more thing is instead of storing each element in the level, maybe canjust the store the entire sum of the levels directly in the list. lets try 
        q = deque([root])
        sumi = 0 
        level = [] 
        res = []
        while q : 
            level = [] 
            for _ in range(len(q)): 
                node = q.popleft() 
                level.append(node.val)
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
            res.append(sum(level))
        
        return res.index(max(res)) + 1




        