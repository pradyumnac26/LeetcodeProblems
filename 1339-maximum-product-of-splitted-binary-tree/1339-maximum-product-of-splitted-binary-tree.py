# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # remove each edge and add the sums of the trees and stre the product somewhere, and then find the maximum. 
        # take the sum of the entire tree. (sum that subtree's node contributes to the entire tree), so that its easy to subtract. 
        # 
        # say we if remove that edge then it would be 1+2+3+4+5 * 6 
        # 1 + 2 + 3 + 4 + 6 * 5 
        # 1 + 2 + 3 + 5 + 6 * 4 
        # 1 + 2 + 4 + 5  * (3+6)
        # *entire sum - sumi)*sumi 
        total = 0 
        def dfs1(root): 
            if root is None : 
                return 0 
            return dfs1(root.left) + dfs1(root.right) + root.val 
        total = dfs1(root)
        print(total)



        def dfs2(root): 
            nonlocal maxi
            if not root : 
                return 0
            lh = dfs2(root.left) 
            rh = dfs2(root.right)
            subtree_sum = lh + rh + root.val
            maxi = max(maxi, (total - subtree_sum)*subtree_sum)
            return subtree_sum
        
        maxi = float('-inf')
        dfs2(root)
        return maxi % (10**9 + 7)








        