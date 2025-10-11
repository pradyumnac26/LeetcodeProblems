class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(i, res) : 
            if i  == len(candidates) : 
                return 
            if sum(res) > target : 
                return 
            print(res)
            if sum(res) == target : 
                x.append(res)
                return 

            backtrack(i, res + [candidates[i]])
            backtrack(i+1, res)

        x = [] 

        backtrack(0, [])
        return x

        