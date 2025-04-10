class Solution:
    def partitionString(self, s: str) -> int:
        z = ""   # current substring
        x = []   # list to store partitions
        
        for i in s:
            if i not in z:
                z += i
            else:
                x.append(z)  
                z = i        
                
        if z:  
            x.append(z)
        
        return len(x)
