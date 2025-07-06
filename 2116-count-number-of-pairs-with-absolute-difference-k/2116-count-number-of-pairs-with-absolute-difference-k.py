class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # abs of nums[i] - nums[j] == k i < j 
        freq = Counter(nums)
        cnt = 0
        for i in freq : 
            cnt = cnt + freq[i]*freq[i+k]
        return cnt

        
        