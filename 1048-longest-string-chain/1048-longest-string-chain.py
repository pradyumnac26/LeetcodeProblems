class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        lsc = [1]*len(words) 
        words.sort(key=len)
        def isPred(x, y) : 
            if len(x) + 1 != len(y) : 
                return False 
            i = j = 0 
            skipped = 0 
            while i < len(x) and j < len(y) : 
                if x[i] == y[j] : 
                    i = i +1 
                    j = j +1 
                else : 
                    skipped+=1 
                    j+=1 
                    if skipped > 1 : 
                        return False
            return True



        for i in range(len(words)-1, -1, -1) : 
            for j in range(i+1, len(words)) : 
                if  isPred(words[i], words[j]) : 
                    lsc[i] = max(lsc[i], 1 + lsc[j]) 
        return max(lsc)




        