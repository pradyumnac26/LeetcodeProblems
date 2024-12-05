class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def sliding(nums, k): 
            l, r = 0,0 
            mpp = defaultdict(int)
            n = len(nums)
            cnt = 0 
            while r < n : 
                mpp[nums[r]] += 1
                while len(mpp) > k : 
                    mpp[nums[l]] -= 1 
                    if mpp[nums[l]] == 0 : 
                        del mpp[nums[l]]
                    l+=1
                cnt =  cnt + (r-l+1)
                r = r + 1
            return cnt
        
        return sliding(nums, k) - sliding(nums, k-1)
        