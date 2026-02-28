from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while st and temperatures[i] > temperatures[st[-1]]:
                j = st.pop()
                ans[j] = i - j
            st.append(i)

        return ans