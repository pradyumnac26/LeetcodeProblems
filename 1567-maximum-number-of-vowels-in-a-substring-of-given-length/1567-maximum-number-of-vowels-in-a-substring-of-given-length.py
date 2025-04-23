# class Solution:
#     def maxVowels(self, s: str, k: int) -> int:
#         l = 0 
#         r = k-1
#         x = "aeiou"
#         maxcnt = float('-inf')
#         maxcnt = 0 
#         while r < len(s): 
#             count = 0 
#             for i in range(l,r+1): 
#                 if s[i] in x : 
#                     count = count + 1 
#                 maxcnt = max(count, maxcnt)
#             l = l +1 
#             r = r +1
#         return maxcnt

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0 
        r = k-1
        x = set("aeiou")
        count = 0 
        max_val = float('-inf')
        for i in range(k): 
            if s[i] in x : 
                count = count + 1 
        max_val = count

        r = k 
        while r < len(s): 
            if s[r] in x : 
                count = count +1
            if s[r-k] in x : 
                count = count -1 
            max_val = max(max_val, count)
            r = r +1
        return max_val 



        



        

        