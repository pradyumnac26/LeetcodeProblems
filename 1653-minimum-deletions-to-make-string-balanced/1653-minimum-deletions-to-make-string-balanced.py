class Solution:
    def minimumDeletions(self, s: str) -> int:
        st = [] 
        cnt = 0 
        for i in range(len(s)): 
            if st and st[-1] == "b" and  s[i] == "a" : 
                st.pop() 
                cnt+=1 
            else : 
                st.append(s[i])
        return cnt 
    
        