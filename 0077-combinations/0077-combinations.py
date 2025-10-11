class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(i, path) : 

            if len(path) == k : 
                res.append(path)
                return 
            if i > n : 
                return 
            for j in range(i, n+1) :
                backtrack(j+1, path + [j])

             



        res = [] 
        backtrack(1, [])
        return res