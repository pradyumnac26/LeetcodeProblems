class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        st = [] 
        cnt = 0 
        for i in range(len(s)): 
            if st and st[-1] > s[i] : 
                st.pop() 
                cnt+=1 
            else : 
                st.append(s[i]) 
        return cnt  

        