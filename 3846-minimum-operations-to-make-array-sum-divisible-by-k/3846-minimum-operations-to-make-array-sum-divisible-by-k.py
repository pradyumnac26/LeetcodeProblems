class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sumi = sum(nums)
        remainder = sumi % k
        return 0 if remainder == 0 else remainder




        



        