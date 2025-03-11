class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi = float("-inf")
        for i in sentences : 
            x = i.split()
            maxi = max(len(x), maxi)
        return maxi
        