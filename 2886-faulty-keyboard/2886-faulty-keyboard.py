class Solution:
    def finalString(self, s: str) -> str:
        fin = "" 
        for i in s : 
            if i == "i" : 
                fin = fin[::-1]

            else : 
                fin = fin + i 
        return fin

        