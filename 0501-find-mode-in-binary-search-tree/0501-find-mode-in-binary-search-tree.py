# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, freq): 
            if root is None: 
                return 
            freq[root.val]+=1
            dfs(root.left, freq)
            dfs(root.right, freq)
        freq = defaultdict(int)
        dfs(root,freq )
        print(freq)

        max_freq = max(freq.values())
        return [key for key, val in freq.items() if val == max_freq]


        