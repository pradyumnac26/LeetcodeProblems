class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set() 
        hmap = defaultdict(bool)
        def backtrack(nums, path, hmap) : 
            if len(path) == len(nums) : 
                res.add(tuple(path))
                return 


            for i in range(len(nums)): 
                if not hmap[i]: 
                    hmap[i] = True 
                    backtrack(nums, path + [nums[i]], hmap )
                    hmap[i] = False 

            



        backtrack(nums, [], hmap)
        return list(res)
        