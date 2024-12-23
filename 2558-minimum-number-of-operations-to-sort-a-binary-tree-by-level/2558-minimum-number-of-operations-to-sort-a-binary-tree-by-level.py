class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def count_swaps(nums: List[int]) -> int:
            swaps = 0
            sorted_nums = sorted(nums)  # Get the sorted version of the array
            
            # Expanded version of idx_map creation
            idx_map = {}
            for i, n in enumerate(nums):
                idx_map[n] = i  # Map the value 'n' to its index 'i' in the original nums list
            
            # Iterate through the array
            for i in range(len(nums)):
                if nums[i] != sorted_nums[i]:  # If the current number is not in its correct position
                    swaps += 1  # A swap is needed
                    
                    # Find the correct index of the value sorted_nums[i] in the original array
                    j = idx_map[sorted_nums[i]]  # The index where sorted_nums[i] is currently located
                    
                    # Swap nums[i] with nums[j]
                    nums[i], nums[j] = nums[j], nums[i]
                    
                    # Update idx_map after the swap
                    idx_map[nums[j]] = j  # Update the new index of nums[j]
                    idx_map[nums[i]] = i  # Update the new index of nums[i]
            
            return swaps

        if not root:
            return 0

        q = deque([root])  # Queue for BFS traversal
        res = 0

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)  # Add left child to the queue
                if node.right:
                    q.append(node.right)  # Add right child to the queue
                level.append(node.val)  # Collect the values at the current level
            
            # Count the minimum swaps required to sort the current level
            res += count_swaps(level)
        return res