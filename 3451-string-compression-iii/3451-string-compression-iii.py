class Solution:
    def compressedString(self, word: str) -> str:

        res = "" 
        count = 1 
        n = len(word)
        ch = word[0]
        for i in range(1, len(word)) : 
            if word[i] == ch and count < 9 : 
                count += 1
            else : 
                res = res + str(count) + ch
                ch = word[i]
                count = 1
        res = res + str(count) + ch
        return res


            


        