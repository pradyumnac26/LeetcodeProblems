class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(i, path) : 

            if len(path) == k : 
                res.append(path)
                return

            if i > n : 
                return 
            backtrack(i+1, path + [i])
            backtrack(i+1, path)


        res = [] 
        backtrack(1, [])
        return res
        