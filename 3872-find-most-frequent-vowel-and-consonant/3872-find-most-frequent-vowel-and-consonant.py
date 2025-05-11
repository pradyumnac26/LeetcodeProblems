class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vmap = defaultdict(int)
        cmap = defaultdict(int)
        for i in s : 
            if i in vowels:
                vmap[i] +=1
            else : 
                cmap[i] += 1 
        max_vowel = max(vmap.values()) if vmap else 0
        max_consonant = max(cmap.values()) if cmap else 0
        return max_vowel + max_consonant
        