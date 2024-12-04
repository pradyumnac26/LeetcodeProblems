class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:





        def slidingwindow(nums, goal):
            l,r,sumi = 0,0,0 
            cnt = 0 

            while r < len(nums) : 
                sumi = sumi + nums[r]
                while (sumi > goal) and l<=r : 
                    sumi = sumi - nums[l] 
                    l = l + 1 
                cnt = cnt + (r-l+1)
                r = r + 1 
            return cnt 

        return slidingwindow(nums, goal) - slidingwindow(nums, goal-1)


        