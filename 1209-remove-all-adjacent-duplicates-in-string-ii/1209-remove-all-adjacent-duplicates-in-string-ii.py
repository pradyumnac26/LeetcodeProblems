class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # deeedbbcccbdaa -> ddbbcccbdaa
        # ddbbbdaa -> dddaa -> aa -> which is the final answer... 
        # so how to approach this.. 
        # we need to keep track of the number, and if it is == k then we neeed to remove those.. 
        # so lets dry run, so maybe we will put a seperate hashmap counter for ease ? lets try.. 
        # no but we need contiguous , so howto do .? 
        st = [] 
        for i in s : 
            if st and st[-1][0] == i : 
                st[-1][1] +=1 
                if st[-1][1] == k : 
                    st.pop() 
            
            else : 
                st.append([i, 1])
        res = "" 
        for i in st : 
            ch, cnt = i 
            res += ch*cnt 
        return res


            


        