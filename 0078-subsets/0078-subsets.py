class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, res) : 
            if i == len(nums) : 
                x.append(res)
                print(res)
                print(x)
                return 


            backtrack(i+1, res + [nums[i]])
            backtrack(i+1, res)
            


        res = [] 
        x = [] 
        backtrack(0, res)
        return x
