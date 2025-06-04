class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        st = []

        for i in range(len(heights) - 1, -1, -1):
            count = 0
            while st and heights[i] > st[-1]:
                st.pop()
                count += 1
            if st:
                count += 1 
            res[i] = count
            st.append(heights[i])

        return res
