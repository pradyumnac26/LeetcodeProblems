class Solution:
    def halveArray(self, nums: List[int]) -> int:
        # we need to reduce the sum of array by half and count the min number of operations.
        # we can also use the reduced weight 
        # so to quickly reduce , we need to pick the maximum element and keep reducing it by half.
        # so not just reduce by half but also after popping we need to insert back in the array and again find the max and reduce by half
        # so since we are finding max in every operation we will use a heap. 
        x = sum(nums)
        op = 0 
        reduced = 0
        for i in range(len(nums)) : 
            nums[i] = -nums[i]
        
        heapq.heapify(nums)
        while reduced < x /2 : 
            a = -heapq.heappop(nums)
            heapq.heappush(nums, -a/2)
            reduced = reduced + a/2
            op = op + 1
        return op
            



        




        