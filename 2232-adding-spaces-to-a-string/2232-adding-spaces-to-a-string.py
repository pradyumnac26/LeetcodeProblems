class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        x = "" 
        j = 0 
        for i in range(len(s)) :
            if j < len(spaces) and i==spaces[j] : 
                x = x + " "
                j+=1
            x = x + s[i]
        
        return x


        