class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_length = 1  


        for i in range(len(nums)):
            curr_and = 0
            for j in range(i, len(nums)):
                if curr_and & nums[j] != 0:
                    break  
                curr_and |= nums[j]  
                max_length = max(max_length, j - i + 1)

        return max_length