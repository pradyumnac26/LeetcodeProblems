from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        total_pairs = 0
        left = 0
        result = 0

        for right in range(len(nums)):
            # Add nums[right] to the window
            total_pairs += freq[nums[right]]
            freq[nums[right]] += 1

            # Shrink from the left while total_pairs >= k
            while total_pairs >= k:
                # All subarrays from current left to end are good
                result += len(nums) - right
                # Remove nums[left] from the window
                freq[nums[left]] -= 1
                total_pairs -= freq[nums[left]]
                left += 1

        return result
