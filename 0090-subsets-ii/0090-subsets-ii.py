class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        def backtrack(i, path): 
            if i == len(nums) : 
                res.add(tuple(path))
                return



            backtrack(i+1, path + [nums[i]])
            backtrack(i+1, path)


        backtrack(0, [])
        return list(res)
        