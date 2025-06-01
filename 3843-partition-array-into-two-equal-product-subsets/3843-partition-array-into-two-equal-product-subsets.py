class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        p = math.prod(nums)
        if p == target*target:
            return True
        return False