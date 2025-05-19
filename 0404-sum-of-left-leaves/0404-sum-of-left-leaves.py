class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            total = 0

            # Check if left child is a leaf
            if node.left and not node.left.left and not node.left.right:
                total += node.left.val

            # Recur left and right
            total += dfs(node.left)
            total += dfs(node.right)

            return total

        return dfs(root)

        
        