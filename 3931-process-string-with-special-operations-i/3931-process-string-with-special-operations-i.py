class Solution:
    def processStr(self, s: str) -> str:
        res = ""
        st = [] 
        for i in s : 
            if i.isalpha() : 
                res = res + i
            elif i == "#" : 
                res = res + res 
            elif i == "%" : 
                res = res[::-1]
            else : 
                res = res[:len(res)-1] 
        return res
        
