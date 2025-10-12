class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, path) : 
            if len(path) == len(nums) : 
                res.append(path)
                return 


            for j in range(i, len(nums)) : 
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i+1, path + [nums[i]])
                nums[i], nums[j] = nums[j], nums[i]


        res = []
        backtrack(0,[])
        return res
        