class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hmap= {2 : "abc", 3 : "def", 4 : "ghi", 5 : "jkl", 6: "mno", 7: "pqrs", 8 : "tuv", 9 : "wxyz"}

        def dfs(i, x): 
            if i == len(digits) : 
                res.append(x) 
                return 

            for j in hmap[int(digits[i])] : 
                dfs(i+1, x+j)
        
        
        res = [] 
        dfs(0, "")
        return res