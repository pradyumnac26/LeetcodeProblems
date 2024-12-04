class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:


        
        def slidingwindow(nums, k):
            l,r = 0,0 
            cnt,sumi = 0,0

            while r < len(nums) : 
                sumi = sumi + nums[r]%2
                while l<=r and sumi > k : 
                    sumi = sumi - nums[l]%2
                    l = l +1
            
                cnt = cnt + r-l+1
                r = r + 1
            return cnt

        return slidingwindow(nums, k) - slidingwindow(nums, k-1)

        