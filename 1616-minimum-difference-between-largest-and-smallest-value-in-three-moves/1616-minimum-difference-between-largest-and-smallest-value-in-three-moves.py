class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # for difference between largest and smallest value to be minimum -> largest should be nearer smallest , so we need to reduce the largest to the smallest value. 
        k = 3 
        # convert first 3 max elements to the min elements
        if len(nums) <= 4 : 
            return 0
        mini_four = sorted(heapq.nsmallest(4, nums))
        max_four = sorted(heapq.nlargest(4, nums))

        res = float('inf')
        for i in range(4): 
            res = min(res,max_four[i]- mini_four[i] )
        return res