from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        def atMostKDistinct(k):
            freq = defaultdict(int)
            l = 0
            count = 0
            for r in range(len(nums)):
                freq[nums[r]] += 1
                while len(freq) > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1
                count += r - l + 1
            return count
        
        total_distinct = len(set(nums))
        return atMostKDistinct(total_distinct) - atMostKDistinct(total_distinct - 1)
