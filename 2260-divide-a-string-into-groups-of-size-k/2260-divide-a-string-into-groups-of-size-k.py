class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        x = [] 
        i = 0
        while i < len(s): 
            x.append(s[i:i+k])
            i = i + k 
        print(x)
        for i in range(len(x)): 
            while len(x[i]) != k : 
                x[i] = x[i] + fill
        return x 
                





        
        