class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        hmap = Counter(nums)
        sumi = 0 
        for key, v in hmap.items() : 
            if v%k == 0 or v == 0 : 
                sumi = sumi + key*v 
        return sumi 

        