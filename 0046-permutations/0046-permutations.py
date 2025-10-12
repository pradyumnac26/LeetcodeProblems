class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        hmap = defaultdict(bool) 
        def backtrack(nums, path, hmap, res): 
            if len(path) == len(nums) :
                res.append(path)
                return  


            for i in range(len(nums)): 
                if not hmap[i] : 
                    hmap[i] = True 
                    backtrack(nums,path + [nums[i]], hmap, res )
                    hmap[i] = False


        backtrack(nums, [], hmap, res) 
        return res
        