class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # have to choose the pair with minimum sum, and replace them with their sum.
        # and have to keep repeating this until the array becomes non-decreasing.
        # so say there is this array [5,2,3,1] -> i find the minimum sums pf pairs meaning of 2-2 element each 
        # so first the sum of mins would be [7,5,4] - so the min is 4 so i replace the index with hich these were summed and replace it with 4.
        # i mean meaning replace the first element index of the pair with the sum , [5,2,4]. have to do th emin pair sum for this -> 5,6 . it is non decreasing.
        # also have to keep track of the count, and return it.
        # first lets writet the core logic , later we can add our conditions.
        # while doing the brute force that when i realised that it is a min heap problem.
        # [7,5,4] 


        res = 0
        minimum = float('inf')
        ind = 0
        while nums != sorted(nums):
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < minimum:
                    minimum = nums[i] + nums[i + 1]
                    ind = i
            nums.pop(ind)
            nums[ind] = minimum
            minimum, ind = float('inf'), 0
            res += 1
        return res
        

            

            
            
            
            
        
        