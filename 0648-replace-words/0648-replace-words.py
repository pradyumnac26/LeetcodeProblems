class TrieNode: 
    def __init__(self): 
        self.children = {} 
        self.isEndWord = False 

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode() 

        for word in dictionary: 
            node = root
            for ch in word:
                if ch not in node.children: 
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.isEndWord = True 

        def startsWith(word): 
            node = root 
            prefix = "" 
            for i in word : 
                if i not in node.children : 
                    return word 
                node = node.children[i] 
                prefix += i

                if node.isEndWord : 
                    return prefix  
            return word


        x = sentence.split()
        ans = [] 
        for i in x : 
            ans.append(startsWith(i))
        return ' '.join(ans) 


        

        