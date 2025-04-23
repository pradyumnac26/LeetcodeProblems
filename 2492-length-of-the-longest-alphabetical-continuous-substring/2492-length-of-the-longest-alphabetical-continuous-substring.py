class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        count = 1
        max_val = 1
        for i in range(len(s)-1): 
            if ord(s[i]) + 1 == ord(s[i+1]): 
                count = count + 1
            else : 
                count = 1 
            max_val = max(max_val, count)

        return max_val

        