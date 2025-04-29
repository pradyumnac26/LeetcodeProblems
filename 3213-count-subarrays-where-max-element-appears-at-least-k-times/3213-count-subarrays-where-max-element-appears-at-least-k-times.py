class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # return the number of subarrays
        # where max element of nums say i call it target appears atleast k times in that subarray. 
        # so say i can do a dry run first
        # I can start with brute force first, 1,3,2,3.

        # final = 0 
        # target = max(nums)
        # for i in range(len(nums)): 
        #     cnt = 0 
        #     for j in range(i, len(nums)): 
        #         if nums[j] == target : 
        #             cnt = cnt + 1 
        #         if cnt >=k : 
        #             final = final + 1  
        # return final
        # now after brute force lets try sliding window cux i feltlike there is no use of tthatfirst loop here.
        # max element appears atleask k times means, find if a number appears atleast k times.
        # clear hashmap , cant do it just with a variable
        l = 0 
        target = max(nums)
        cnt = 0 
        final = 0 
        for r in range(len(nums)): 
            if nums[r] == target : 
                cnt = cnt + 1 
            
            while cnt >=k : 
                final += len(nums) - r
                if nums[l] == target : 
                    cnt = cnt - 1 
                l = l + 1 
        return final

            

            


        