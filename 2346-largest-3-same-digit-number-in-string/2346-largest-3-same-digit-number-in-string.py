class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                cand = num[i] * 3          # e.g., "777"
                if cand > ans:             # lexicographic works for digits
                    ans = cand
        return ans
