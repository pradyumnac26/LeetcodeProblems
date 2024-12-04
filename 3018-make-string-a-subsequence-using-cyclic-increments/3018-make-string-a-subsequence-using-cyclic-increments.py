class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0 
        for char in str1 : 
            if i < len(str2) and (-ord(char) + ord(str2[i]))%26 < 2 : 
                i = i + 1

        return i == len(str2)
        