class Solution:
    def isValid(self, word: str) -> bool:
        vowels = set("aeiou")
        cnt = 0 
        alp = False
        vow = False
        if len(word) < 3 : 
            return False
        for i in word : 
            if not i.isalnum():
                return False 
            if i.isalpha() and i.lower() not in vowels: 
                alp =True 
            if i.lower() in vowels: 
                vow = True
        return vow and alp



            


        