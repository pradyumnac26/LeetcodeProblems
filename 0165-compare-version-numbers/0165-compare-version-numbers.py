class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        x = version1.split(".")
        y = version2.split(".")

        for i in range(max(len(x), len(y))) : 
            if i <len(x) : 
                rev1 = int(x[i]) 
            else : 
                rev1 = 0 
            if i < len(y) : 
                rev2 = int(y[i]) 
            else : 
                rev2 = 0 
            
            if rev1 > rev2 : 
                return 1
            elif rev2 > rev1: 
                return -1
        return 0                        


        