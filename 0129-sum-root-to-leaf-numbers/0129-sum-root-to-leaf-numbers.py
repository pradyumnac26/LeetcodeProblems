class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0  # to store the final sum

        def dfs(node, path):
            if not node:
                return

            path += str(node.val)

            if not node.left and not node.right:
                self.total += int(path)
                return

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return self.total
