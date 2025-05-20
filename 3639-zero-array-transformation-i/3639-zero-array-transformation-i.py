from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        
        # Initialize a difference array to 0
        diff = [0] * (n + 1)
        
        # Apply the range updates from the queries
        for li, ri in queries:
            diff[li] += 1
            if ri + 1 < n:
                diff[ri + 1] -= 1
        
        # Apply the difference array to nums and check if we can make it a zero array
        current_decrement = 0
        for i in range(n):
            current_decrement += diff[i]  # Get the cumulative decrement for index i
            nums[i] -= current_decrement  # Apply the decrement to nums[i]
            
            # If nums[i] goes below 0, we reset it to 0
            if nums[i] < 0:
                nums[i] = 0
        
        # After all decrements, check if the array is completely zero
        return all(num == 0 for num in nums)
