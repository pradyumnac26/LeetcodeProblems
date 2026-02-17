class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]: 
        def dfs(i,path) : 
            if len(path) == len(nums) :
                res.append(path )
                return

            for j in range(i,len(nums)) : 
                nums[i], nums[j] = nums[j], nums[i]

                dfs(i+1, path + [nums[i]]) 
                nums[i], nums[j] = nums[j] , nums[i] 




        res = [] 
        dfs(0, [])
        return res