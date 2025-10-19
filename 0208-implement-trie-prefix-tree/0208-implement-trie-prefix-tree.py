class TrieNode:
    def __init__(self):
        self.children = {} 
        self.isendword = False 

class Trie:


    def __init__(self):
        self.root = TrieNode() 
        

    def insert(self, word: str) -> None:
        node = self.root
        for i in word : 
            if i not in node.children : 
                node.children[i] = TrieNode() 
            node = node.children[i]
        node.isendword = True 
        

    def search(self, word: str) -> bool:
        node = self.root
        for i in word : 
            if i not in node.children : 
                return False 
            node = node.children[i] 
        if node.isendword : 
            return True 
        else : 
            return False 


    def startsWith(self, prefix: str) -> bool:
        node = self.root 
        for i in prefix : 
            if i not in node.children : 
                return False 
            node = node.children[i] 
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)