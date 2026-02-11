class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # append d in stack, append e in stack and then when u see the 3rd e u realise oh okay have already inserted 2 so lets pop k-1 times, and then u append d and then b twice and then c 3 times u realise its 
        # equal to k-1 in stack alreready so u pop k-1 times and now u enter b and u see k-1 are equal in stack and again u pop, and now u see d and then.  aa.
        st = [] # stores pairs of ch and count 
        for ch in s : 
            if st and st[-1][0] == ch : 
                st[-1][1] += 1
                if st[-1][1] == k : 
                    st.pop()
            
            else : 
                st.append([ch, 1])
        res = ""
        for ch, count in st : 
            res = res + count*ch

        return res


        