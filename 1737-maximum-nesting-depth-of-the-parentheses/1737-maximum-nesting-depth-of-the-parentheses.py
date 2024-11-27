class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0 
        maxi = 0 
        for i in s : 
            if i == '(' : 
                cnt +=1
            elif i == ')' : 
                cnt -= 1
            
            maxi = max(maxi, cnt)
        return maxi

        