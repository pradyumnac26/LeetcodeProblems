class Solution:
    def removeZeros(self, n: int) -> int:
        z = str(n) 
        x = "" 
        for i in z : 
            if i != '0' : 
                x = x + i
        return int(x)
                
