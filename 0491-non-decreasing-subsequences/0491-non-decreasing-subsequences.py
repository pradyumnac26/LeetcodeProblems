class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        def backtracking(i, x) : 

            if i == len(nums) : 
                if len(x) >= 2 : 
                    result.add(tuple(x))
                return 
            
            if not x or nums[i] >= x[-1] : 
                x.append(nums[i])
                backtracking(i+1, x)
                x.pop()
            backtracking(i+1, x)



        result = set() 
        x = []
        backtracking(0, x)
        return [list(seq) for seq in result] 