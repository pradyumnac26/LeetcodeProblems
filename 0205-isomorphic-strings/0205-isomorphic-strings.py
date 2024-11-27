class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t) : 
            return False
        s_to_t = {} 
        t_to_s = {} 
        for schar, tchar in zip(s,t) : 
            if schar in s_to_t : 
                if s_to_t[schar] != tchar : 
                    return False
            else : 
                s_to_t[schar] = tchar
            
            if tchar in t_to_s : 
                if t_to_s[tchar] != schar : 
                    return False 
            else : 
                t_to_s[tchar] = schar
        return True

        