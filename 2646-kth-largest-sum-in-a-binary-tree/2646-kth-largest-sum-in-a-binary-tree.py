from collections import deque
import heapq

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        minHeap = [] 

        while q: 
            level_sum = 0 
            for i in range(len(q)): 
                node = q.popleft()
                level_sum += node.val
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            
            # Push the level sum into the heap only once per level
            heapq.heappush(minHeap, level_sum)
            if len(minHeap) > k: 
                heapq.heappop(minHeap)

        return -1 if len(minHeap) < k else minHeap[0]
