class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # we use a deque and a sliding window approach for this.
        # we need to maintain a monotonically decreasing queue. 
        q = deque() # store indices
        l = 0 
        res = [] 
        for r in range(len(nums)): 
            while q and  nums[r] > nums[q[-1]]: 
                q.pop()
            q.append(r)
            if l > q[0] : 
                q.popleft()
            if (r+1) >= k : 
                res.append(nums[q[0]])
                l = l +1

        return res




        