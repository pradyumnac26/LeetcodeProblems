class Solution:
    def getDirections(self, root, startValue, destValue):
        def dfs(node, value, path):
            if not node:
                return False
            if node.val == value:
                return True

            path.append('L')
            if dfs(node.left, value, path):
                return True
            path.pop()

            path.append('R')
            if dfs(node.right, value, path):
                return True
            path.pop()

            return False

        path_to_start = []
        path_to_dest = []
        dfs(root, startValue, path_to_start)
        dfs(root, destValue, path_to_dest)

        # Find where paths diverge
        i = 0
        while i < len(path_to_start) and i < len(path_to_dest) and path_to_start[i] == path_to_dest[i]:
            i += 1

        # Move up from start to LCA, then down to destination
        return 'U' * (len(path_to_start) - i) + ''.join(path_to_dest[i:])
