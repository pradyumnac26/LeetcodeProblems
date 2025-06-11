class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hmap = {} 
        for i in range(len(nums)): 
            if nums[i] not in hmap : 
                hmap[nums[i]] = 1 
            else : 
                hmap[nums[i]]+=1 
        maxi = max(hmap.values())
        cnt = 0
        for k, v in hmap.items(): 
            if v == maxi : 
                cnt += v
        return cnt


        