class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        hmap = Counter(nums)
        for k,v in hmap.items() : 
            if v == 1 : 
                return k

        