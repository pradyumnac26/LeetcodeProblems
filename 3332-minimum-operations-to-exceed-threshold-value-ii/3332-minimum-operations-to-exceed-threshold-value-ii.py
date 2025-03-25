class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # ill create nums as a heap , and then i need to keep removing 2 elements which are the 2 smallest in the heap.
        # this can be done using the heappop gunction which picks the root which is usually the min element in a min- heap.
        # then calculate min*2 + max of the 2 and insertt in heap by doing heappush. 
        # so how many times to keep doing this ? this hs to be done until all the elementsin nums are geater than the value k.
        # so how do we determine or loop through that ? 
        # maybe i can 

        op = 0 
        n = len(nums)
        heapq.heapify(nums)
        while nums[0] <k :

            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x,y)*2 + max(x,y))
            op = op + 1
        return op
        

        
        