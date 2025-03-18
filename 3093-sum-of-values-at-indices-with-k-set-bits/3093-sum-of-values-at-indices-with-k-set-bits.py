class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        s = 0 
        for i in range(len(nums)) : 
            x = bin(i)[2:]
            if x.count('1') == k : 
                s = s + nums[i]
        return s


        