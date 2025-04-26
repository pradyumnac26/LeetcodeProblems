class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_minK = -1       # Last index where nums[i] == minK
        last_maxK = -1       # Last index where nums[i] == maxK
        last_invalid = -1    # Last index where nums[i] is out of [minK, maxK]
        count = 0            # Total number of valid subarrays

        for i, num in enumerate(nums):
            # Update last_invalid if num is out of [minK, maxK]
            if num < minK or num > maxK:
                last_invalid = i
            
            # Update last_minK if num == minK
            if num == minK:
                last_minK = i

            # Update last_maxK if num == maxK
            if num == maxK:
                last_maxK = i

            # Calculate how many valid subarrays end at index i
            count += max(0, min(last_minK, last_maxK) - last_invalid)

        return count
