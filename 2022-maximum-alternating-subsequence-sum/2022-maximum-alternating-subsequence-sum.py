from functools import lru_cache
from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        @lru_cache(None)
        def backtrack(i: int, is_even: bool) -> int:
            if i == len(nums):
                return 0

            # Choose current num
            if is_even:
                take = nums[i] + backtrack(i + 1, False)
            else:
                take = -nums[i] + backtrack(i + 1, True)

            # Skip current num
            skip = backtrack(i + 1, is_even)

            return max(take, skip)

        return backtrack(0, True)
