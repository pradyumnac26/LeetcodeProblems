class Solution:
    def replaceDigits(self, s: str) -> str:
        x = "" 
        for i in range(len(s)): 
            if i %2 == 0: 
                x = x + s[i] 
            else : 
                z = ord(s[i-1] ) + int(s[i])
                x = x + chr(z)
        return x


        