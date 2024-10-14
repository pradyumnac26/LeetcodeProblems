class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        x = sentence.split()
        print(x)
        count = 0 
        for i in range(len(x)):
            if x[i][-1] == x[(i+1)%len(x)][0] : 
                count+=1

        

        if count == len(x) : 
            return True 
        else : 
            return False

        