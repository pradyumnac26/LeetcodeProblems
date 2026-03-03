class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # smallest number means we need small number, and then if we see a big number we shouldnt do anything..
        # but if we have a bigger number ? then remove the bigger number , and put the smaller number.. 
        st = [] 
        for i in range(len(num)) : 
            while st and st[-1]  > int(num[i]) and k > 0 : 
                st.pop() 
                k = k - 1
            st.append(int(num[i]))
        
        while k > 0 and st : 
            st.pop()
            k = k - 1

        res = "".join(str(x) for x in st).lstrip("0")
        return res if res else "0"




        