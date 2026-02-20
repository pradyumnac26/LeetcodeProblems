from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []   # stack of indices
        maxi = 0

        for i in range(len(heights)):
            while st and heights[st[-1]] > heights[i]:
                h = heights[st.pop()]    
                nse = i                      
                pse = st[-1] if st else -1     

                width = nse - pse - 1
                maxi = max(maxi, h * width)

            st.append(i)


        n = len(heights)
        while st:
            h = heights[st.pop()]
            nse = n
            pse = st[-1] if st else -1
            width = nse - pse - 1
            maxi = max(maxi, h * width)

        return maxi