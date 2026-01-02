class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2 
        # n + 1 unique elements, so say len of array is 6 , then 4 unique elements, ad 1 element repeated n times so 3 times, return element repeated n times. 
        hmap = Counter(nums)
        for k, v in hmap.items() : 
            if v > 1 : 
                return k 

        