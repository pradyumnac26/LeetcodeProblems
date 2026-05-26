class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s1 = set()
        s2 = set()
        cnt = 0 
        for i in word:
            if i.islower() : 
                s1.add(i)
            elif i.isupper() : 
                s2.add(i)
        
        for i in s1 : 
            if i.upper() in s2 : 
                cnt+=1 
        return cnt



        

        