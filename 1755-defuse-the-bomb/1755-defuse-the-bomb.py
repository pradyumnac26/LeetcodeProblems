class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        res=[0]*N
        l = 0 
        curr = 0 
        for r in range(N+abs(k)) : 
            curr += code[r%N]

            if r-l+1 > abs(k) : 
                curr-= code[l%N]
                l = (l+1)%N

            if r-l+1 == abs(k) : 
                if k > 0 : 
                    res[(l-1)%N] = curr
                elif k < 0 : 
                    res[(r+1)%N] = curr 
        return res


        