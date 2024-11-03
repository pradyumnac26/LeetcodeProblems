class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = [] 
        z = "" 
        for i in s : 
            if i.isalpha() : 
                ans.append(i)
        for i in range(len(s)) : 
            if s[i].isalpha() : 
                z = z + ans.pop()
            else : 
                z = z + s[i] 
        return z
        





