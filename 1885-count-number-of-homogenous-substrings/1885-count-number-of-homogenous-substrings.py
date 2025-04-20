class Solution:
    def countHomogenous(self, s: str) -> int:
        # homogenous substring means , if all the chars in the sustrig are the same.
        # a= 1 cnt=1 , b=1 cnt=2, b=2cnt = 4, 
        cnt = 1 
        same = 1 
        MOD = 10**9 + 7
        for i in range(1, len(s)): 
            if s[i] == s[i-1] : 
                same = same +1 
            else : 
                same = 1
            cnt = (cnt + same)%MOD
        return cnt



        