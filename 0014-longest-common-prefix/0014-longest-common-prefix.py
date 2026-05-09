class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = sorted(strs) 
        first = s[0]
        last = s[-1] 
        res = "" 
        for i in range(min(len(first), len(last))): 
            if first[i] == last[i]: 
                res = res + first[i]
            else : 
                break 
        return res

        
        