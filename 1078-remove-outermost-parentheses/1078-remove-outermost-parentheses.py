class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        x = "" 
        cnt = 0 
        for i in s : 
            if i == '(': 
                if cnt > 0 : 
                    x = x + i
                cnt +=1 
            elif i == ")" : 
                cnt -=1 
                if cnt > 0 : 
                    x = x + i
        return x 
        