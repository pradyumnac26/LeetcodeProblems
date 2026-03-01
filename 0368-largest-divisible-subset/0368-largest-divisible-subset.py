from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)

        lds = [1] * n
        nxt = [-1] * n
        res = [] 

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0:
                    if 1 + lds[j] > lds[i]:
                        lds[i] = 1 + lds[j]
                        nxt[i] = j

        start = lds.index(max(lds))
        while start != -1 : 
            res.append(nums[start]) 
            start = nxt[start]
        return res

