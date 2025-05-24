class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        b = [] 
        vis = [0]*26
        for word in range(len(words)): 
            for ch in range(len(words[word])): 
                if words[word][ch] == x : 
                    b.append(word)
                    break
        return b

        