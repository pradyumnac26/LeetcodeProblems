class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        ind = [] 
        for i in range(len(s1)) :
            if s1[i] != s2[i] : 
                ind.append(i)
            
            if len(ind) > 2 : 
                return False
        if len(ind) == 2 : 
            i, j = ind 
            if s1[i] == s2[j] and s1[j] == s2[i] : 
                return True 
            else : 
                return False

        return len(ind) == 0





        