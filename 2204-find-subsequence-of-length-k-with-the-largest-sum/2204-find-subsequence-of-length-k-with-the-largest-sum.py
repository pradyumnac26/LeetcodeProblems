from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Pair values with their indices
        indexed = [(num, i) for i, num in enumerate(nums)]
        # Sort by value descending
        top_k = sorted(indexed, key=lambda x: -x[0])[:k]
        # Sort selected k items by index to preserve order
        top_k_sorted = sorted(top_k, key=lambda x: x[1])
        # Extract only the values
        return [num for num, i in top_k_sorted]
