# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        idx = 0
        q = deque([(root, idx)])
        maxi = 0 
        while q : 
            level = 1
            first = q[0][1]
            last = q[-1][1] 
            maxi = max(maxi, last - first+1)

            for _ in range(len(q)) : 
                node, i = q.popleft()
                level = level+1 
                if node.left : 
                    q.append((node.left, (2*i)))
                if node.right : 
                    q.append((node.right, 2*i+1))
        return maxi


        