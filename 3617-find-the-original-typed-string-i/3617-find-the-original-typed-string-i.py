class Solution:
    def possibleStringCount(self, word: str) -> int:
        # how many repeatable chars 
        cnt = 1 
        same = 0 
        for i in range(1, len(word)): 
            if word[i] == word[i-1]: 
                cnt+=1 
        return cnt 


        