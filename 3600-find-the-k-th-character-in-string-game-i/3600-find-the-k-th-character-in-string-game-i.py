class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k : 
            for i in range(len(word)) : 
                word = word + chr(ord(word[i]) + 1)

        print(word)
        return word[k-1]

    


        